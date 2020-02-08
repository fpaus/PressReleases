import bs4
import requests

from Helpers.FileHelper import FileHelper
from WebPages.Articles.ArgentinaArticle import ArgentinaArticle
from WebPages.GenericPage import GenericPage


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
        self.file = 'Argentina.csv'
        self.header = ['date', 'title', 'text']
        self.fileHelper = FileHelper()

    def loop_items(self, bs, i=1):
        print(i)
        arts = bs.select(self.articleLink)
        if len(arts) > 0:
            for art in arts:
                url = self.rootURL + art.contents[1].attrs['href']
                self.articles.append(url)
                article = ArgentinaArticle(url, self.fileHelper)
                article.save_article(self.file)
                print(article.get_title())
                print(article.get_date())
                print(article.get_text)
            res = requests.get('{}{}{}'.format(self.url, self.nextPage, i))
            res.raise_for_status()
            bs = bs4.BeautifulSoup(res.text, features="html.parser")
            i = i + 1
            self.loop_items(bs, i)

    def list_articles(self):
        self.loop_items(self.soup)
        return self.articles

    def save_articles(self):
        self.fileHelper.generate_header(self.file, self.header)
        self.loop_items(self.soup)
        return self.articles
