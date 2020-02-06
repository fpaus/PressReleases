import bs4
import requests
from Helpers.FileHelper import FileHelper

class ArgentinaArticle(object):
    def __init__(self, articleUrl, fileHelper):
        self.url = articleUrl
        self.date = '.date-display-single'
        self.text = '.field.field-name-body.field-type-text-with-summary.field-label-hidden'
        self.title = 'page-header'
        res = requests.get(self.url)
        res.raise_for_status()
        self.soup = bs4.BeautifulSoup(res.text, features="html.parser")
        self.fileHelper = fileHelper
    
    def blacklist(self):
        return [
        '[document]',
        'noscript',
        'header',
        'html',
        'meta',
        'head',
        'input',
        'script',
        # there may be more elements you don't want, such as "style", etc.
    ]

    def getTitle(self):
        return self.soup.find('h1', {'class': self.title}).getText()

    def getDate(self):
        date = self.soup.select(self.date)[0].contents[0]
        return date

    def getText(self):
        output = ''
        text = self.soup.find_all('p')
        ##text = text.find_all('p')
        for p in text:
            paragraph = p.getText()
            output = output + ' (newLine) ' + paragraph
        return output

    def saveArticle(self, file):
        self.fileHelper.appendData(file, [self.getDate(), self.getTitle(), self.getText()])