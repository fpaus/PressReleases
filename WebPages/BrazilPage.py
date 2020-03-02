import bs4
import requests

from Helpers.FileHelper import FileHelper
from WebPages.Articles.BrazilArticle import BrazilArticle
from WebPages.GenericPage import GenericPage


class BrazilPage(GenericPage):
    def __init__(self):
        super().__init__()
        self.rootURL = 'http://www.itamaraty.gov.br/pt-BR/notas-a-imprensa'
        self.url = 'http://www.itamaraty.gov.br/pt-BR/notas-a-imprensa'
        res = requests.get(self.url)
        res.raise_for_status()
        self.soup = bs4.BeautifulSoup(res.text, features="html.parser")
        self.articleLink = '.tileHeadline'
        self.articles = []
        self.nextPage = '?start='
        self.file = 'Brazil.csv'
        self.fileHelper = FileHelper()

    def loop_items(self, bs, i=0):
        print(i)
        arts = bs.select(self.articleLink)
        if len(arts) > 0:
            for art in arts:
                url = self.rootURL + art.contents[1].attrs['href']
                print(url)
                self.articles.append(url)
                article = BrazilArticle(url, self.fileHelper)
                article.save_article(self.file)
                print(article.get_date())
            res = requests.get('{}{}{}'.format(self.url, self.nextPage, i))
            res.raise_for_status()
            bs = bs4.BeautifulSoup(res.text, features="html.parser")
            i = i + 15
            self.loop_items(bs, i)

    def list_articles(self):
        self.loop_items(self.soup)
        return self.articles

    def save_articles(self):
        self.fileHelper.generate_header(self.file, self.header)
        self.loop_items(self.soup)
        return self.articles
