import bs4
import requests

from Helpers.FileHelper import FileHelper
from WebPages.Articles.GenericArticle import GenericArticle
from WebPages.Articles.GenericArticle import replace_new_line_and_tab


class BushArticle(GenericArticle):
    _file_helper: FileHelper

    def __init__(self, article_url: str, file_helper: FileHelper, title: str):
        super().__init__(article_url, file_helper)
        self._date = ['p', {'class': 'dettagli_articolo_cont'}]
        self._text = ['div', {'itemprop': 'articleBody'}]
        self._title = title
        res = requests.get(self._url)
        res.raise_for_status()
        self._soup = bs4.BeautifulSoup(res.text, features="html.parser").find('td', {'class': 'content-font-style'})

    def _get_title(self):
        try:
            title = self._soup.find('h1').getText()
        except:
            title = self._title
        print(title)
        return replace_new_line_and_tab(title)

    def _get_date(self):
        import re
        #date = self._soup.find_all('font')[3].getText()
        fonts = self._soup.find_all('font')
        for font in fonts:
            date = font.getText()
            m = re.search('[A-z]* [0-9]{1,2}, [0-9]{4}', date)
            if m is not None:
                print(date)
                return replace_new_line_and_tab(date)

    def _get_text(self):
        output = ''
        text = [p.getText() for p in self._soup.find_all('p') if p.getText() != '']
        for p in text:
            paragraph = "{} (newline) ".format(
                replace_new_line_and_tab(p))
            output = output + paragraph
        return output
