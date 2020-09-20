import bs4
import requests

from WebPages.Articles.PeruArticle import PeruArticle
from WebPages.GenericPage import GenericPage


# 575126091

class PeruPage(GenericPage):
    def __init__(self):
        self._file = 'Peru'
        super().__init__()
        self._root_url = 'https://www.gob.pe'
        self._url = 'https://www.gob.pe/busquedas?contenido[]=noticias&institucion[]=rree&reason=sheet&sheet=1&tipo_noticia[]=3-comunicado&tipo_noticia[]=1-nota-de-prensa'
        res = requests.get(self._url)
        res.raise_for_status()
        self._soup = bs4.BeautifulSoup(res.text, features="html.parser")
        self._article_link = 'track-ga-click'
        self._next_page = ''
        self._next = '.pagination__next'

    def _loop_items(self):
        arts = self._soup.findAll("a", {'class': self._article_link})
        if len(arts) > 0:
            for art in arts:
                partial_url = art.attrs['href']
                url = self._root_url + partial_url
                if url not in self._articles and "/busquedas?" not in url:
                    print(url)
                    article = PeruArticle(url, self._file_helper)
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
