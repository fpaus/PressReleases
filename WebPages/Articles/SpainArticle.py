import bs4
import requests

from Helpers.FileHelper import FileHelper
from WebPages.Articles.GenericArticle import GenericArticle
from WebPages.Articles.GenericArticle import replace_new_line_and_tab


class SpainArticle(GenericArticle):
    _file_helper: FileHelper

    def __init__(self, article_url: str, file_helper: FileHelper):
        super().__init__(article_url, file_helper)
        self._date = '.date.fecha'
        self._text = 'content contenidoLayout'
        self._title = 'antetitulo'
        res = requests.get(self._url, headers={'User-Agent': 'Mozilla/5.0'})
        res.raise_for_status()
        self._soup = bs4.BeautifulSoup(res.text, features="html.parser")

    def _get_title(self):
        title = replace_new_line_and_tab(self._soup.find('div', {'class': self._title}).getText())
        print("title:", title)
        return title

    def _get_date(self):
        date = replace_new_line_and_tab(self._soup.select(self._date)[0].contents[0])
        print("date:", date)
        return date

    def _get_text(self):
        return replace_new_line_and_tab(self._soup.find('div', {'class': self._text}).getText())
