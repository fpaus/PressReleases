import bs4
import requests

from Helpers.FileHelper import FileHelper


class ArgentinaArticle(object):
    fileHelper: FileHelper

    def __init__(self, article_url, file_helper):
        self.url = article_url
        self.date = '.date-display-single'
        self.text = '.field.field-name-body.field-type-text-with-summary.field-label-hidden'
        self.title = 'page-header'
        res = requests.get(self.url)
        res.raise_for_status()
        self.soup = bs4.BeautifulSoup(res.text, features="html.parser")
        self.fileHelper = file_helper

    def get_title(self):
        return self.soup.find('h1', {'class': self.title}).getText()

    def get_date(self):
        date = self.soup.select(self.date)[0].contents[0]
        return date

    @property
    def get_text(self):
        output = ''
        text = self.soup.find_all('p')
        for p in text:
            paragraph = p.get_text
            output = output + ' (newLine) ' + paragraph
        return output

    def save_article(self, file):
        self.fileHelper.append_data(file, [self.get_date(), self.get_title(), self.get_text])
