import bs4
import requests

from WebPages.Articles.ParaguayArticle import ParaguayArticle
from WebPages.GenericPage import GenericPage


# 575126091

class ParaguayPage(GenericPage):
    def __init__(self):
        self._file = 'Paraguay'
        super().__init__()
        self._root_url = 'http://www.itamaraty.gov.br/pt-BR/notas-a-imprensa'
        self._url = 'https://www.mre.gov.py/index.php/galeria/comunicados'
        res = requests.get(self._url)
        res.raise_for_status()
        self._soup = bs4.BeautifulSoup(res.text, features="html.parser")
        self._article_link = '.ccm-block-page-list-title'
        self._next_page = '?start='

    def _loop_items(self, i=0):
        print(i)
        arts = self._soup.select(self._article_link)
        if len(arts) > 0:
            for art in arts:
                url = art.find('a').attrs['href']
                if url not in self._articles:
                    article = ParaguayArticle(url, self._file_helper)
                    article.save_article(self._file)
                    self._articles.append(url)
                    print(article._get_date())

    def _list_articles(self):
        self._loop_items()
        return self._articles
