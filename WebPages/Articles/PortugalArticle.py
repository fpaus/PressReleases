import bs4
import requests

from Helpers.FileHelper import FileHelper
from WebPages.Articles.GenericArticle import GenericArticle
from WebPages.Articles.GenericArticle import replace_new_line_and_tab


class PortugalArticle(GenericArticle):
    _file_helper: FileHelper

    def __init__(self, article_url: str, file_helper: FileHelper, title: str):
        super().__init__(article_url, file_helper)
        self._date = '.date-display-single'
        self._text = '.field.field-name-body.field-type-text-with-summary.field-label-hidden'
        self._title = title
        res = requests.get(self._url)
        res.raise_for_status()
        self._soup = bs4.BeautifulSoup(res.text, features="html.parser")

    def _get_title(self):
        # title = self._soup.find('div', {'class': self.title}).getText()
        return replace_new_line_and_tab(self._title)

    def _get_date(self):
        date = self._soup.select('.published')
        date = date[0]
        date = date.find('time')
        date = date.attrs['datetime']
        return replace_new_line_and_tab(date)

    def _get_text(self):
        paragraph = self._soup.find('div', {'itemprop': 'articleBody'})
        output = ''
        text = paragraph.find_all('p')
        for p in text:
            paragraph = "{} (newline) ".format(replace_new_line_and_tab(p.getText()))
            output = output + paragraph
        return output
