import bs4
import requests

from Helpers.FileHelper import FileHelper
from WebPages.Articles.GenericArticle import GenericArticle
from WebPages.Articles.GenericArticle import replace_new_line_and_tab


class TrumpArticle(GenericArticle):
    _file_helper: FileHelper

    def __init__(self, article_url: str, file_helper: FileHelper):
        super().__init__(article_url, file_helper)
        self._date = ['p', {'class': 'dettagli_articolo_cont'}]
        self._text = ['div', {'itemprop': 'articleBody'}]
        res = requests.get(self._url)
        res.raise_for_status()
        self._soup = bs4.BeautifulSoup(res.text, features="html.parser")

    def _get_title(self):
        title = self._soup.find('h1', {'class': 'featured-content__headline stars-above'}).getText()
        print(title)
        return replace_new_line_and_tab(title)

    def _get_date(self):
        date = self._soup.find('p', {'class': 'article-meta__publish-date'}).getText()
        print(date)
        return replace_new_line_and_tab(date)

    def _get_text(self):
        output = ''
        paragraphs = self._soup.find('div', {'class': 'entry-content'})
        text = [p.getText() for p in paragraphs.find_all('p') if p.getText() != '']
        for p in text:
            paragraph = "{} (newline) ".format(
                replace_new_line_and_tab(p))
            output = output + paragraph
        return output
