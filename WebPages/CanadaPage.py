import bs4
import requests
import warnings

from WebPages.Articles.CanadaArticle import CanadaArticle
from WebPages.GenericPage import GenericPage


class CanadaPage(GenericPage):
    def __init__(self):
        warnings.filterwarnings("ignore")
        self._file = 'Canada'
        super().__init__()
        self._root_url = 'https://www.canada.ca'
        self._url = 'https://www.canada.ca/en/news/advanced-news-search/news-results.html?_=1590959909718&dprtmnt=departmentofforeignaffairstradeanddevelopment&start=&end='
        res = requests.get(self._url, verify=False)
        res.raise_for_status()
        self._soup = bs4.BeautifulSoup(res.text, features="html.parser")

    def _loop_items(self, i=1):
        print(i)
        arts = self._soup.find_all('article', {'class': 'item'})
        if len(arts) > 0:
            for art in arts:
                partial_url = art.find('a').attrs['href']
                url = partial_url
                if url not in self._articles:
                    self._articles.append(url)
                    date = art.find('time').attrs['datetime']
                    article = CanadaArticle(url, self._file_helper, date)
                    article.save_article(self._file)
        next_page = self._soup.find('a', {'rel': 'next'})
        if next_page is not None:
            res = requests.get(f"{self._root_url}{next_page.attrs['href']}")
            res.raise_for_status()
            self._soup = bs4.BeautifulSoup(res.text, features="html.parser")
            self._loop_items(i+1)

    def _list_articles(self):
        self._loop_items()
        return self._articles
