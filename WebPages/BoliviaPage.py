import bs4
import requests

from WebPages.Articles.BoliviaArticle import BoliviaArticle
from WebPages.GenericPage import GenericPage


# 575126091

class BoliviaPage(GenericPage):
    def __init__(self):
        self._file = 'Bolivia'
        super().__init__()
        self._root_url = 'http://www.cancilleria.gob.bo'
        self._url = 'http://www.cancilleria.gob.bo/webmre/comunicados'
        res = requests.get(self._url)
        res.raise_for_status()
        self._soup = bs4.BeautifulSoup(res.text, features="html.parser")
        self._article_link = "views-row"
        self._next_page = ''
        self._next = 'li.next.last'

    def _loop_items(self):
        arts = self._soup.findAll("div", {'class': self._article_link})
        if len(arts) > 0:
            for art in arts:
                partial_url = art.find('a').attrs['href']
                url = self._root_url + partial_url
                print(url)
                article = BoliviaArticle(url, self._file_helper)
                article.save_article(self._file)
                self._articles.append(url)
                print(article._get_date())
            self._next_page = self._soup.select(self._next)[0].select('a')[0].attrs['href']
            print(self._next_page)
            res = requests.get('{}{}'.format(self._root_url, self._next_page))
            res.raise_for_status()
            self._soup = bs4.BeautifulSoup(res.text, features="html.parser")
            self._loop_items()

    def _list_articles(self):
        self._loop_items()
        return self._articles
