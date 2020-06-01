import bs4
import requests

from Helpers.FileHelper import FileHelper
from WebPages.Articles.GenericArticle import GenericArticle
from WebPages.Articles.GenericArticle import replace_new_line_and_tab


class ColombiaArticle(GenericArticle):
    _file_helper: FileHelper

    def __init__(self, article_url: str, file_helper: FileHelper):
        super().__init__(article_url, file_helper)
        self._date = 'date-display-single'
        self._text = 'field field-name-body field-type-text-with-summary field-label-hidden'
        self._title = 'pane-title'
        res = requests.get(self._url)
        res.raise_for_status()
        self._soup = bs4.BeautifulSoup(res.text, features="html.parser")

    def _get_title(self):
        title = self._soup.find('h2', {'class': self._title}).getText()
        return replace_new_line_and_tab(title)

    def _get_date(self):
        date = self._soup.find('span', {'class': self._date}).getText()
        return replace_new_line_and_tab(date)

    def _get_text(self):
        return replace_new_line_and_tab(self._soup.find('div', {'class': self._text}).getText())
