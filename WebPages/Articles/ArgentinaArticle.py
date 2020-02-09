import bs4
import requests

from Helpers.FileHelper import FileHelper
from WebPages.Articles.GenericArticle import GenericArticule


class ArgentinaArticle(GenericArticule):
    fileHelper: FileHelper

    def __init__(self, article_url: str, file_helper: FileHelper):
        super().__init__(article_url, file_helper)
        self.date = '.date-display-single'
        self.text = '.field.field-name-body.field-type-text-with-summary.field-label-hidden'
        self.title = 'page-header'
        res = requests.get(self.url)
        res.raise_for_status()
        self.soup = bs4.BeautifulSoup(res.text, features="html.parser")

    def get_title(self):
        return self.soup.find('h1', {'class': self.title}).getText()

    def get_date(self):
        date = self.soup.select(self.date)[0].contents[0]
        return date

    def get_text(self):
        output = ''
        text = self.soup.find_all('p')
        for p in text:
            paragraph = p.getText()
            output = "{} (newLine) {}".format(output, paragraph)
        return output
