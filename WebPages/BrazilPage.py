import bs4
import requests

from WebPages.Articles.BrazilArticle import BrazilArticle
from WebPages.GenericPage import GenericPage


# 575126091

class BrazilPage(GenericPage):
    def __init__(self):
        self._file = 'Brazil'
        super().__init__()
        self._root_url = 'http://www.itamaraty.gov.br/pt-BR/notas-a-imprensa'
        self.url = 'http://www.itamaraty.gov.br/pt-BR/notas-a-imprensa'
        res = requests.get(self.url)
        res.raise_for_status()
        self.soup = bs4.BeautifulSoup(res.text, features="html.parser")
        self.articleLink = '.tileHeadline'
        self.nextPage = '?start='

    def _loop_items(self, i=2975):
        print(i)
        arts = self.soup.select(self.articleLink)
        if len(arts) > 0:
            for art in arts:
                url = self._root_url + art.contents[1].attrs['href']
                if url not in self._articles:
                    article = BrazilArticle(url, self._file_helper)
                    article.save_article(self._file)
                    self._articles.append(url)
            res = requests.get('{}{}{}'.format(self.url, self.nextPage, i))
            res.raise_for_status()
            self.soup = bs4.BeautifulSoup(res.text, features="html.parser")
            i = i + 15
            self._loop_items(i)

    def _list_articles(self):
        self._loop_items()
        return self._articles
