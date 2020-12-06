import bs4
import requests

from WebPages.Articles.CubaArticle import CubaArticle
from WebPages.GenericPage import GenericPage


class CubaPage(GenericPage):
    def __init__(self):
        self._file = 'Cuba'
        super().__init__()
        self._root_url = 'http://www.minrex.gob.cu'
        self._url = 'http://www.minrex.gob.cu/es/declaraciones-del-minrex?page={}'

        self._article_link = '.fusion-post-content-wrapper'

    def _loop_items(self, i=0):
        print(i)
        res = requests.get(self._url.format(i), verify=False)
        res.raise_for_status()
        self._soup = bs4.BeautifulSoup(res.text, features="html.parser")
        arts = self._soup.find_all('h2', {'class': 'node__title'})
        if len(arts) > 0:
            for art in arts:
                article_url = art.find('a').attrs['href']
                url = '{}{}'.format(self._root_url, article_url)
                if url not in self._articles:
                    date = art.find('time').attrs['datetime'].replace('"', '').replace('\\', '').replace("'", '')
                    article = CubaArticle(url, self._file_helper, date)
                    article.save_article(self._file)
                    self._articles.append(url)
                    print('url:', url)
                    print('date:', date)
            i = i + 1
            self._loop_items(i)

    def _list_articles(self):
        self._loop_items()
        return self._articles
