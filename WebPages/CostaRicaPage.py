import bs4
import requests

from WebPages.Articles.CostaRicaArticle import CostaRicaArticle
from WebPages.GenericPage import GenericPage


# 575126091

class CostaRicaPage(GenericPage):
    def __init__(self):
        self._file = 'CostaRica'
        super().__init__()
        self._root_url = 'https://www.rree.go.cr/'
        self._url = 'https://www.rree.go.cr/?sec=servicios&cat=prensa&cont=593&id={}'

    def _loop_items(self):
        for i in range(6700):
            try:
                url = self._url.format(i)
                if url not in self._articles:
                    article = CostaRicaArticle(url, self._file_helper)
                    article.save_article(self._file)
                    self._articles.append(url)
                    print(url)
            except Exception as e:
                print(i, "Error:", e)

    def _list_articles(self):
        self._loop_items()
        return self._articles
