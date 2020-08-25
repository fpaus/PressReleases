import bs4
import requests

from WebPages.Articles.EcuadorArticle import EcuadorArticle
from WebPages.GenericPage import GenericPage


# 575126091

class EcuadorPage(GenericPage):
    def __init__(self):
        self._file = 'Ecuador'
        super().__init__()
        self._root_url = 'http://www.cancilleria.gob.bo'
        self._url = 'https://www.cancilleria.gob.ec/category/noticias/'
        res = requests.get(self._url, verify=False)
        res.raise_for_status()
        self._soup = bs4.BeautifulSoup(res.text, features="html.parser")
        self._article_link = "contenido-comunica"
        self._next_page = ''
        self._next = '.nav-next'

    def _loop_items(self):
        arts = self._soup.find("div", {'id': self._article_link})
        links = arts.find_all('a')
        for a in links:
            if a.get_text() != 'Siguientes →' and a.get_text() != '← Anteriores':
                url = a.attrs['href']
                if url not in self._articles:
                    date = a.find('span', {'class': 'time'}).getText()
                    print(url)
                    article = EcuadorArticle(url, self._file_helper, date)
                    article.save_article(self._file)
                    self._articles.append(url)
                    print(article._get_date())
        self._next_page = arts.select(self._next)[0].select('a')[0].attrs['href']
        print(self._next_page)
        res = requests.get(self._next_page, verify=False)
        res.raise_for_status()
        self._soup = bs4.BeautifulSoup(res.text, features="html.parser")
        self._loop_items()

    def _list_articles(self):
        self._loop_items()
        return self._articles
