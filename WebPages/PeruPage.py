import bs4
import requests

from WebPages.Articles.PeruArticle import PeruArticle
from WebPages.GenericPage import GenericPage
from WebPages.Selenium.PeruPage import PeruPage as SeleniumPage

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
        selenium = SeleniumPage()
        return selenium.save_articles()

    def _list_articles(self):
        self._loop_items()
        return self._articles
