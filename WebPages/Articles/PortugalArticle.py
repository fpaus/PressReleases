import bs4
import requests

from Helpers.FileHelper import FileHelper
from WebPages.Articles.GenericArticle import GenericArticle
from WebPages.Articles.GenericArticle import replace_new_line_and_tab


class PortugalArticle(GenericArticle):
    fileHelper: FileHelper

    def __init__(self, article_url: str, file_helper: FileHelper, title: str):
        super().__init__(article_url, file_helper)
        self.date = '.date-display-single'
        self.text = '.field.field-name-body.field-type-text-with-summary.field-label-hidden'
        self.title = title
        res = requests.get(self.url)
        res.raise_for_status()
        self.soup = bs4.BeautifulSoup(res.text, features="html.parser")

    def get_title(self):
        # title = self.soup.find('div', {'class': self.title}).getText()
        return replace_new_line_and_tab(self.title)

    def get_date(self):
        date = self.soup.select('.published')
        date = date[0]
        date = date.find('time')
        date = date.attrs['datetime']
        return replace_new_line_and_tab(date)

    def get_text(self):
        paragraph = self.soup.find('div', {'itemprop': 'articleBody'})
        output = ''
        text = paragraph.find_all('p')
        for p in text:
            paragraph = "{} (newline) ".format(replace_new_line_and_tab(p.getText()))
            output = output + paragraph
        return output
