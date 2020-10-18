import bs4
import requests

from Helpers.FileHelper import FileHelper
from WebPages.Articles.GenericArticle import GenericArticle
from WebPages.Articles.GenericArticle import replace_new_line_and_tab


class ItalyArticle(GenericArticle):
    _file_helper: FileHelper

    def __init__(self, article_url: str, file_helper: FileHelper):
        super().__init__(article_url, file_helper)
        self._date = ['p', {'class': 'dettagli_articolo_cont'}]
        self._text = ['div', {'itemprop': 'articleBody'}]
        self._title = ['h1', {'itemprop': 'headline'}]
        res = requests.get(self._url)
        res.raise_for_status()
        self._soup = bs4.BeautifulSoup(res.text, features="html.parser")

    def _get_title(self):
        title = self._soup.find(self._title[0], self._title[1]).getText()
        return self._translate(replace_new_line_and_tab(title))

    def _get_date(self):
        date = self._soup.find(self._date[0], self._date[1]).getText()
        return self._translate(replace_new_line_and_tab(date))

    def _get_text(self):
        paragraph = self._soup.find(self._text[0], self._text[1])
        output = ''
        text = paragraph.find_all('p')
        for p in text:
            paragraph = "{} (newline) ".format(
                self._translate(replace_new_line_and_tab(p.getText())))
            output = output + paragraph
        return output
