import bs4
import requests

from WebPages.Articles.PortugalArticle import PortugalArticle
from WebPages.GenericPage import GenericPage


# 575126091

class PortugalPage(GenericPage):
    def __init__(self):
        self._file = 'Portugal'
        super().__init__()
        self._root_url = 'https://www.portaldiplomatico.mne.gov.pt'
        self._url = 'https://www.portaldiplomatico.mne.gov.pt/comunicacao-e-media/comunciados-de-imprensa'
        res = requests.get(self._url)
        res.raise_for_status()
        self._soup = bs4.BeautifulSoup(res.text, features="html.parser")
        self._article_link = '.page-header'
        self._next_page = ''
        self._next = '.pagination-next'

    def _loop_items(self):
        arts = self._soup.select(self._article_link)
        if len(arts) > 0:
            for art in arts:
                partial_url = art.find('a').attrs['href']
                title = art.find('a').getText()
                url = self._root_url + partial_url
                print(url)
                if url not in self._articles:
                    article = PortugalArticle(url, self._file_helper, title)
                    article.save_article(self._file)
                    self._articles.append(url)
                    print(article._get_date())
            self._next_page = self._soup.select(self._next)[0].select('a')[0].attrs['href']
            print(self._next_page)
            res = requests.get('{}{}'.format(self._root_url, self._next_page))
            res.raise_for_status()
            self._soup = bs4.BeautifulSoup(res.text, features="html.parser")
            self._loop_items()

    def _list_articles(self):
        self._loop_items()
        return self._articles
