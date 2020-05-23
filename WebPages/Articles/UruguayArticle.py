import bs4
import requests

from Helpers.FileHelper import FileHelper
from WebPages.Articles.GenericArticle import GenericArticle
from WebPages.Articles.GenericArticle import replace_new_line_and_tab


class UruguayArticle(GenericArticle):
    fileHelper: FileHelper

    def __init__(self, article_url: str, file_helper: FileHelper):
        super().__init__(article_url, file_helper)
        self.date = 'Page-date'
        self.text = 'Page-document'
        self.title = 'Page-Title'
        res = requests.get(self.url)
        res.raise_for_status()
        self.soup = bs4.BeautifulSoup(res.text, features="html.parser")

    def get_title(self):
        title = self.soup.find('h2', {'class': self.title}).getText()
        return replace_new_line_and_tab(title)

    def get_date(self):
        date = self.soup.find('div', {'class': self.date}).getText()
        return replace_new_line_and_tab(date)

    def get_text(self):
        document = self.soup.find('div', {'class': self.text})
        output = ''
        text = document.find_all('p')
        for p in text:
            paragraph = "{} (newline) ".format(replace_new_line_and_tab(p.getText()))
            output = output + paragraph
        return output
