import bs4
import requests

from WebPages.Articles.PortugalArticle import PortugalArticle
from WebPages.GenericPage import GenericPage


# 575126091

class PortugalPage(GenericPage):
    def __init__(self):
        self.file = 'Portugal'
        super().__init__()
        self.rootURL = 'https://www.portaldiplomatico.mne.gov.pt'
        self.url = 'https://www.portaldiplomatico.mne.gov.pt/comunicacao-e-media/comunciados-de-imprensa'
        res = requests.get(self.url)
        res.raise_for_status()
        self.soup = bs4.BeautifulSoup(res.text, features="html.parser")
        self.articleLink = '.page-header'
        self.nextPage = ''
        self.next = '.pagination-next'

    def loop_items(self):
        arts = self.soup.select(self.articleLink)
        if len(arts) > 0:
            for art in arts:
                partial_url = art.find('a').attrs['href']
                url = self.rootURL + partial_url
                print(url)
                if url not in self.articles:
                    article = PortugalArticle(url, self.fileHelper)
                    article.save_article(self.file)
                    self.articles.append(url)
                    print(article.get_date())
            self.nextPage = self.soup.select(self.next)[0].select('a')[0].attrs['href']
            res = requests.get('{}{}'.format(self.rootURL, self.nextPage))
            res.raise_for_status()
            self.soup = bs4.BeautifulSoup(res.text, features="html.parser")
            self.loop_items()

    def list_articles(self):
        self.loop_items()
        return self.articles
