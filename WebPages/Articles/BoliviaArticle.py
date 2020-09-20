import bs4
import requests

from Helpers.FileHelper import FileHelper
from WebPages.Articles.GenericArticle import GenericArticle
from WebPages.Articles.GenericArticle import replace_new_line_and_tab


class BoliviaArticle(GenericArticle):
    _file_helper: FileHelper

    def __init__(self, article_url: str, file_helper: FileHelper):
        super().__init__(article_url, file_helper)
        self._date = '.date-display-single'
        self._text = 'description institution-document__description'
        self._title = "text-center"
        res = requests.get(self._url)
        res.raise_for_status()
        self._soup = bs4.BeautifulSoup(res.text, features="html.parser")

    def _get_title(self):
        title = self._soup.find('h2', {'class': self._title}).getText()
        return replace_new_line_and_tab(title)

    def _get_date(self):
        date = self._soup.find('p', {'class' : 'rteright'})
        if date is None:
            date = self._soup.find('p', {'class' : 'rtecenter'})
        if date is None:
            return ""
        date = date.getText()
        return replace_new_line_and_tab(date)

    def _get_text(self):
        paragraph = self._soup.find_all('div', {'class': 'col-md-12 col-lg-12'})
        p = paragraph[5].getText('\n')
        return "{} (newline) ".format(replace_new_line_and_tab(p))
