from WebPages.Articles.TrumpArticle import TrumpArticle
import bs4
import requests

from Helpers.FileHelper import FileHelper
from WebPages.Articles.GenericArticle import GenericArticle
from WebPages.Articles.GenericArticle import replace_new_line_and_tab


class ObamaArticle(GenericArticle):
    _file_helper: FileHelper

    def __init__(self, article_url: str, file_helper: FileHelper, title: str):
        super().__init__(article_url, file_helper)
        self._date = ['p', {'class': 'dettagli_articolo_cont'}]
        self._text = ['div', {'itemprop': 'articleBody'}]
        self._title = title
        res = requests.get(self._url)
        res.raise_for_status()
        self._soup = bs4.BeautifulSoup(res.text, features="html.parser")

    def _get_title(self):
        try:
            title = self._soup.find('h2', {'id': 'page-title'}).getText()
        except:
            title = self._title
        print(title)
        return replace_new_line_and_tab(title)

    def _get_date(self):
        date_html = self._soup.find('div', {'id': 'date_long'})
        if(date_html is None):
            date_html = self._soup.find('div', {'id': 'press_article_date_created'})
        if(date_html is None):
            self = self.refresh()
            return self._get_date()
        date = date_html.getText()
        print(date)
        return replace_new_line_and_tab(date)

    def _get_text(self):
        output = ''
        paragraphs = self._soup.find('div', {'id': 'centerblock'})
        if paragraphs is None:
            paragraphs = self._soup.find('div', {'class': 'field-items'})
        if paragraphs is None:
            self = self.refresh()
            return self._get_text()
        text = [p.getText() for p in paragraphs.find_all('p') if p.getText() != '']
        for p in text:
            paragraph = "{} (newline) ".format(
                replace_new_line_and_tab(p))
            output = output + paragraph
        return output

    def refresh(self):
        url = self._soup.find('meta').attrs['content'].split('=')[-1]
        self = ObamaArticle(url, self._file_helper, self._title)
        return self
