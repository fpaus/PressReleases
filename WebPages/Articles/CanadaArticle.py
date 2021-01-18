import bs4
import requests

from Helpers.FileHelper import FileHelper
from WebPages.Articles.GenericArticle import GenericArticle
from WebPages.Articles.GenericArticle import replace_new_line_and_tab


class CanadaArticle(GenericArticle):
    _file_helper: FileHelper

    def __init__(self, article_url: str, file_helper: FileHelper, date: str):
        super().__init__(article_url, file_helper)
        self._date = date
        res = requests.get(self._url)
        res.raise_for_status()
        self._soup = bs4.BeautifulSoup(res.text, features="html.parser")

    def _get_title(self):
        title = self._soup.find('h1', {'id': 'wb-cont'}).getText()
        print(title)
        return replace_new_line_and_tab(title)

    def _get_date(self):
        print(self._date)
        return replace_new_line_and_tab(self._date)

    def _get_text(self):
        body_paragraph = self._soup.find(
            'div', {'class': 'cmp-text'})
        if body_paragraph is None:
            body_paragraph = self._soup.find(
                'div', {'id': 'news-release-container'})
        if body_paragraph is None:
            body_paragraph = self._soup.find(
                'div', {'class': 'mwsbodytext text parbase section'})
        paragraphs = body_paragraph.getText()
        return replace_new_line_and_tab(paragraphs)
