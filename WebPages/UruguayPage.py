import bs4
import requests

from WebPages.Articles.UruguayArticle import UruguayArticle
from WebPages.GenericPage import GenericPage


class UruguayPage(GenericPage):
    def __init__(self):
        self.file = 'Uruguay'
        super().__init__()
        self.rootURL = 'https://www.gub.uy'
        self.url = 'https://www.gub.uy/ministerio-relaciones-exteriores/comunicacion/comunicados?field_tematica_target_id=All&field_publico_target_id=All&year=all&month=all&page=0'
        res = requests.get(self.url)
        res.raise_for_status()
        self.soup = bs4.BeautifulSoup(res.text, features="html.parser")
        self.articleLink = '.Media-body h3'
        self.nextPage = '&page='

    def loop_items(self, i=1):
        print(i)
        arts = self.soup.select(self.articleLink)
        if len(arts) > 0:
            for art in arts:
                partial_url = art.find('a').attrs['href']
                url = self.rootURL + partial_url
                if url not in self.articles:
                    self.articles.append(url)
                    article = UruguayArticle(url, self.fileHelper)
                    article.save_article(self.file)
                    print(article.get_date())
            res = requests.get('{}{}{}'.format(self.url, self.nextPage, i))
            res.raise_for_status()
            self.soup = bs4.BeautifulSoup(res.text, features="html.parser")
            i = i + 1
            self.loop_items(i)

    def list_articles(self):
        self.loop_items()
        return self.articles


