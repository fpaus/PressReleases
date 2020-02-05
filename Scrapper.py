import requests
import bs4
from WebPages.GenericPage import GenericPage


class Scrapper(object):
    def __init__(self, page: GenericPage):
        """
        :type page: GenericPage
        """
        self.page = page

    def searchMultiple(self):
        pass

    def articles(self):
        return self.page.list_articles()