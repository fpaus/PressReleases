import bs4
import requests

from Helpers.FileHelper import FileHelper
from WebPages.Articles.GenericArticle import GenericArticle
from WebPages.Articles.GenericArticle import replace_new_line_and_tab


class MexicoArticle(GenericArticle):
    _file_helper: FileHelper

    def __init__(self, article_url: str, file_helper: FileHelper, date: str):
        super().__init__(article_url, file_helper)
        self._date = date
        self._text = 'article-body'
        self._title = "bottom-buffer"
        res = requests.get(self._url)
        res.raise_for_status()
        self._soup = bs4.BeautifulSoup(res.text, features="html.parser")

    def _get_title(self):
        title = self._soup.find('h1', {'class': self._title}).getText()
        return replace_new_line_and_tab(title)

    def _get_date(self):
        return replace_new_line_and_tab(self._date)

    def _get_text(self):
        paragraph = self._soup.find_all('div', {'class': self._text})
        text = ''
        for p in paragraph:
            text = text + p.getText('\n')
        return "{} (newline) ".format(replace_new_line_and_tab(text))
