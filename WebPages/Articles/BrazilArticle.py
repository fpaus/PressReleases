import bs4
import requests

from Helpers.FileHelper import FileHelper
from WebPages.Articles.GenericArticle import GenericArticle
from WebPages.Articles.GenericArticle import replace_new_line_and_tab


class BrazilArticle(GenericArticle):
    _file_helper: FileHelper

    def __init__(self, article_url: str, file_helper: FileHelper):
        super().__init__(article_url, file_helper)
        self._date = '.create'
        self._text = 'articleBody'
        self._title = 'documentFirstHeading'
        res = requests.get(self._url)
        res.raise_for_status()
        self._soup = bs4.BeautifulSoup(res.text, features="html.parser")

    def _get_title(self):
        title = self._soup.find('h1', {'class': self._title}).getText()
        return replace_new_line_and_tab(title)

    def _get_date(self):
        date = self._soup.select(self._date)[0].contents[3].getText()
        return replace_new_line_and_tab(date)

    def _get_text(self):
        text = self._soup.find('div', {'itemprop': self._text}).getText()
        return replace_new_line_and_tab(text)
