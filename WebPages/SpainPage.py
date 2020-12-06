from datetime import date
from datetime import timedelta
import bs4
import requests

from Helpers.FileHelper import FileHelper
from WebPages.Articles.SpainArticle import SpainArticle
from WebPages.GenericPage import GenericPage
from WebPages.Selenium.SpainPage import SpainPage as Selenium

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
        selenium = SeleniumPage()
        return selenium.save_articles()

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
