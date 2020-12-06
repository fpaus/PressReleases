import bs4
import requests

from WebPages.Articles.MexicoArticle import MexicoArticle
from WebPages.GenericPage import GenericPage


class MexicoPage(GenericPage):
    def __init__(self):
        self._file = 'Mexico'
        super().__init__()
        self._root_url = 'https://www.gob.mx'
        self._url = 'https://www.gob.mx/sre/es/archivo/prensa?category=Selecciona+una+categor%C3%ADa&filter_id=&filter_origin=archive&idiom=es&order=DESC&page={}&style=th&tags=&utf8=%E2%9C%93&year='
        # res = requests.get(self._url)
        # res.raise_for_status()
        # self._soup = bs4.BeautifulSoup(res.text, features="html.parser")
        self._article_link = '.fusion-post-content-wrapper'

    def _loop_items(self, i=1):
        print(i)
        res = requests.get(self._url.format(i))
        res.raise_for_status()
        self._soup = bs4.BeautifulSoup(res.text, features="html.parser")
        arts = self._soup.find_all('article')
        if len(arts) > 0:
            for art in arts:
                article_url = art.find('a').attrs['href'].replace('"', '').replace('\\', '')
                url = '{}{}'.format(self._root_url, article_url)
                if url not in self._articles:
                    date = art.find('time').attrs['datetime'].replace('"', '').replace('\\', '').replace("'", '')
                    article = MexicoArticle(url, self._file_helper, date)
                    article.save_article(self._file)
                    self._articles.append(url)
                    print('url:', url)
                    print('date:', date)
            i = i + 1
            self._loop_items(i)

    def _list_articles(self):
        self._loop_items()
        return self._articles
