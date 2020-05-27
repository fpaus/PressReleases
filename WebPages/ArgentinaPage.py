import bs4
import requests

from WebPages.Articles.ArgentinaArticle import ArgentinaArticle
from WebPages.GenericPage import GenericPage


class ArgentinaPage(GenericPage):
    def __init__(self):
        self._file = 'Argentina'
        super().__init__()
        self._root_url = 'https://www.cancilleria.gob.ar'
        self._url = 'https://www.cancilleria.gob.ar/es/actualidad/noticias'
        res = requests.get(self._url)
        res.raise_for_status()
        self._soup = bs4.BeautifulSoup(res.text, features="html.parser")
        self._article_link = '.masonry-item'
        self._next_page = '?page='

    def _loop_items(self, i=1):
        print(i)
        arts = self._soup.select(self._article_link)
        if len(arts) > 0:
            for art in arts:
                url = self._root_url + art.contents[1].attrs['href']
                if url not in self._articles:
                    self._articles.append(url)
                    article = ArgentinaArticle(url, self._file_helper)
                    article.save_article(self._file)
            res = requests.get('{}{}{}'.format(self._url, self._next_page, i))
            res.raise_for_status()
            self._soup = bs4.BeautifulSoup(res.text, features="html.parser")
            i = i + 1
            self._loop_items(i)

    def _list_articles(self):
        self._loop_items()
        return self._articles


