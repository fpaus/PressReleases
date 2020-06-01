from datetime import date
from datetime import timedelta
import bs4
import requests

from Helpers.FileHelper import FileHelper
from WebPages.Articles.SpainArticle import SpainArticle
from WebPages.GenericPage import GenericPage


class SpainPage(GenericPage):
    def __init__(self):
        self._file = 'Spain'
        super().__init__()
        self._root_url = 'http://www.exteriores.gob.es/Portal/es/SalaDePrensa'
        self._url = 'http://www.exteriores.gob.es/Portal/es/SalaDePrensa/NotasDePrensa/Paginas/NotasdePrensa.aspx'
        self._max_former_format = 553
        self._partial_former_url = '/NotasDePrensa/Paginas/Articulos/Comunicado{}.aspx'
        self._first_date_new_format = date(2013, 3, 30)
        self._partial_new_url = '/Comunicados/Paginas/{}_COMUNICADOS/{}_COMU{}.aspx'

    def _loop_items(self):
        for comu in range(1, self._max_former_format + 1):
            url = self._root_url + self._partial_former_url.format(comu)
            if url not in (self._articles):
                try:
                    article = SpainArticle(url, self._file_helper)
                    article.save_article(self._file)
                    print(article._get_date())
                    self._articles.append(url)
                except Exception as e:
                    print(e)
                    print(e.with_traceback())
                    print("error in {}".format(url))
        for comu in range(1, 500):
            year = 2013
            while year == self._first_date_new_format.year:
                article_date = '{}{:02d}{:02d}'.format(self._first_date_new_format.year,
                                                       self._first_date_new_format.month,
                                                       self._first_date_new_format.day)
                try:
                    url = self._root_url + self._partial_new_url.format(year, article_date, comu)
                    if url not in (self._articles):
                        article = SpainArticle(url, self._file_helper)
                        article.save_article(self._file)
                        print(article._get_date())
                        self._articles.append(url)
                        self._first_date_new_format = self._first_date_new_format + timedelta(days=1)
                except:
                    self._first_date_new_format = self._first_date_new_format + timedelta(days=1)
        for year in range(2014, 2021):
            exist_articles = True
            comu = 1
            self._first_date_new_format = date(2014, 1, 1)
            while exist_articles:
                article_date = '{}{:02d}{:02d}'.format(self._first_date_new_format.year,
                                                       self._first_date_new_format.month,
                                                       self._first_date_new_format.day)
                try:
                    comu, url = self._get_article_new_format(article_date, comu, year)
                    print(url)
                except:
                    try:
                        com = '{:03d}'.format(comu)
                        comu, url = self._get_article_new_format(article_date, com, year)
                    except:
                        self._first_date_new_format = self._first_date_new_format + timedelta(days=1)
                        print("No ok")
                        exist_articles = self._first_date_new_format.year == year

    def _get_article_new_format(self, article_date, comu, year):
        url = self._root_url + self._partial_new_url.format(year, article_date, comu)
        print(url)
        article = SpainArticle(url, self._file_helper)
        article.save_article(self._file)
        print("ok")
        print(article._get_date())
        self._articles.append(url)
        print(comu)
        comu = comu + 1
        return comu, url

    def _list_articles(self):
        self._loop_items()
        return self._articles
