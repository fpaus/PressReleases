from datetime import date
from datetime import timedelta
import bs4
import requests


from Helpers.FileHelper import FileHelper
from WebPages.Articles.SpainArticle import SpainArticle
from WebPages.GenericPage import GenericPage


class SpainPage(GenericPage):
    def __init__(self):
        self.file = 'Spain'
        super().__init__()
        self.rootURL = 'http://www.exteriores.gob.es/Portal/es/SalaDePrensa'
        self.url = 'http://www.exteriores.gob.es/Portal/es/SalaDePrensa/NotasDePrensa/Paginas/NotasdePrensa.aspx'
        self.maxFormerFormat = 553
        self.partialFormerUrl = '/NotasDePrensa/Paginas/Articulos/Comunicado{}.aspx'
        self.__first_date_new_format__ = date(2013, 3, 30)
        self.partialNewUrl = '/Comunicados/Paginas/{}_COMUNICADOS/{}_COMU{}.aspx'


    def loop_items(self):
        for comu in range(1, self.maxFormerFormat + 1):
            url = self.rootURL + self.partialFormerUrl.format(comu)
            if url not in (self.articles):
                try:
                    article = SpainArticle(url, self.fileHelper)
                    article.save_article(self.file)
                    print(article.get_date())
                    self.articles.append(url)
                except Exception as e:
                    print(e)
                    print(e.with_traceback())
                    print("error in {}".format(url))
        for comu in range(1, 500):
            year = 2013
            while year == self.__first_date_new_format__.year:
                article_date = '{}{:02d}{:02d}'.format(self.__first_date_new_format__.year, self.__first_date_new_format__.month,
                                                       self.__first_date_new_format__.day)
                try:
                    url = self.rootURL + self.partialNewUrl.format(year, article_date, comu)
                    if url not in (self.articles):
                        article = SpainArticle(url, self.fileHelper)
                        article.save_article(self.file)
                        print(article.get_date())
                        self.articles.append(url)
                        self.__first_date_new_format__ = self.__first_date_new_format__ + timedelta(days=1)
                except:
                    self.__first_date_new_format__ = self.__first_date_new_format__ + timedelta(days=1)
        for year in range(2014, 2021):
            exist_articles = True
            comu = 1
            self.__first_date_new_format__ = date(2014, 1, 1)
            while exist_articles:
                article_date = '{}{:02d}{:02d}'.format(self.__first_date_new_format__.year, self.__first_date_new_format__.month,
                                                       self.__first_date_new_format__.day)
                try:
                    comu, url = self.__get_article_new_format__(article_date, comu, year)
                    print(url)
                except:
                    try:
                        com = '{:03d}'.format(comu)
                        comu, url = self.__get_article_new_format__(article_date, com, year)
                    except:
                        self.__first_date_new_format__ = self.__first_date_new_format__ + timedelta(days=1)
                        print("No ok")
                        exist_articles = self.__first_date_new_format__.year == year

    def __get_article_new_format__(self, article_date, comu, year):
        url = self.rootURL + self.partialNewUrl.format(year, article_date, comu)
        print(url)
        article = SpainArticle(url, self.fileHelper)
        article.save_article(self.file)
        print("ok")
        print(article.get_date())
        self.articles.append(url)
        print(comu)
        comu = comu + 1
        return comu, url

    def list_articles(self):
        self.loop_items()
        return self.articles


