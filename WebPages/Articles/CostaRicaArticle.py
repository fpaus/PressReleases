import warnings

import bs4
import requests

from Helpers.FileHelper import FileHelper
from WebPages.Articles.GenericArticle import GenericArticle
from WebPages.Articles.GenericArticle import replace_new_line_and_tab


class CostaRicaArticle(GenericArticle):
    _file_helper: FileHelper

    def __init__(self, article_url: str, file_helper: FileHelper):
        super().__init__(article_url, file_helper)
        self._date = 'details'
        self._text = 'article animated fadeIn'
        self._title = ''
        warnings.filterwarnings("ignore")
        res = requests.get(self._url, verify=False)
        res.raise_for_status()
        self._soup = bs4.BeautifulSoup(res.text, features="html.parser")

    def _get_title(self):
        title = self._soup.find('h1').getText()
        return replace_new_line_and_tab(title)

    def _get_date(self):
        date = self._soup.find('span', {'class': self._date}).getText()
        return replace_new_line_and_tab(date)

    def _get_text(self):
        paragraph = self._soup.find('article', {'class': self._text})
        output = ''
        text = paragraph.find_all('p')
        for p in text:
            paragraph = "{} (newline) ".format(replace_new_line_and_tab(p.getText()))
            output = output + paragraph
        return output
