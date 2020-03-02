import bs4
import requests

from Helpers.FileHelper import FileHelper
from WebPages.Articles.GenericArticle import GenericArticule
from WebPages.Articles.GenericArticle import replace_new_line_and_tab


class BrazilArticle(GenericArticule):
    fileHelper: FileHelper

    def __init__(self, article_url: str, file_helper: FileHelper):
        super().__init__(article_url, file_helper)
        self.date = '.create'
        self.text = 'articleBody'
        self.title = 'documentFirstHeading'
        res = requests.get(self.url)
        res.raise_for_status()
        self.soup = bs4.BeautifulSoup(res.text, features="html.parser")

    def get_title(self):
        title = self.soup.find('h1', {'class': self.title}).getText()
        return replace_new_line_and_tab(title)

    def get_date(self):
        date = self.soup.select(self.date)[0].contents[3].getText()
        return replace_new_line_and_tab(date)

    def get_text(self):
        text = self.soup.find('div', {'itemprop': self.text}).getText()
        return replace_new_line_and_tab(text)