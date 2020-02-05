import bs4
import requests

from WebPages.GenericPage import GenericPage
from WebPages.Articles.ArgentinaArticle import ArgentinaArticle

class ArgentinaPage(GenericPage):
    def __init__(self):
        super().__init__()
        self.rootURL = 'https://www.cancilleria.gob.ar'
        self.url = 'https://www.cancilleria.gob.ar/es/actualidad/noticias'
        res = requests.get(self.url)
        res.raise_for_status()
        self.soup = bs4.BeautifulSoup(res.text, features="html.parser")
        self.articleLink = '.masonry-item'
        self.articles = []
        self.nextPage = '?page='

    def loop_items(self, bs, i=1):
        print(i)
        arts = bs.select(self.articleLink)
        if len(arts) > 0:
            for art in arts:
                url=self.rootURL + art.contents[1].attrs['href']
                self.articles.append(url)
                article = ArgentinaArticle(url)
                print(article.getTitle())
                print(article.getDate())
                print(article.getText())
            res = requests.get('{}{}{}'.format(self.url, self.nextPage, i))
            res.raise_for_status()
            bs = bs4.BeautifulSoup(res.text, features="html.parser")
            i = i + 1
            self.loop_items(bs, i)

    def list_articles(self):
        self.loop_items(self.soup)
        return self.articles
