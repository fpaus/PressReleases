import bs4
import requests

from Helpers.FileHelper import FileHelper
from WebPages.Articles.GenericArticle import GenericArticule


def replace_new_line_and_tab(text: str):
    return text.strip().replace('\t', '').replace('\r', '').replace('\n', ' (newline) ')


class SpainArticle(GenericArticule):
    fileHelper: FileHelper

    def __init__(self, article_url: str, file_helper: FileHelper):
        super().__init__(article_url, file_helper)
        self.date = '.date.fecha'
        self.text = 'content contenidoLayout'
        self.title = 'antetitulo'
        res = requests.get(self.url, headers={'User-Agent': 'Mozilla/5.0'})
        res.raise_for_status()
        self.soup = bs4.BeautifulSoup(res.text, features="html.parser")

    def get_title(self):
        print("title")
        return replace_new_line_and_tab(self.soup.find('div', {'class': self.title}).getText())

    def get_date(self):
        print("date")
        date = replace_new_line_and_tab(self.soup.select(self.date)[0].contents[0])
        return date

    def get_text(self):
        print("text")
        return replace_new_line_and_tab(self.soup.find('div', {'class': self.text}).getText())
