import bs4
import requests
import warnings

from WebPages.Articles.TrumpArticle import TrumpArticle
from WebPages.GenericPage import GenericPage


class TrumpPage(GenericPage):
    def __init__(self):
        warnings.filterwarnings("ignore")
        self._file = 'Trump'
        super().__init__()
        self._root_url = 'https://2009-2017.state.gov'
        self._url = 'https://www.state.gov/press-releases/'
        res = requests.get(self._url, verify=False)
        res.raise_for_status()
        self._soup = bs4.BeautifulSoup(res.text, features="html.parser")
        self._article_link = '.Media-body h3'
        self._next_page = '&page='

    def _loop_items(self, i=1):
        print(i)
        arts = self._soup.find_all('li', {'class': 'collection-result'})
        if len(arts) > 0:
            for art in arts:
                partial_url = art.find('a').attrs['href']
                url = partial_url
                if url not in self._articles:
                    self._articles.append(url)
                    article = TrumpArticle(url, self._file_helper)
                    article.save_article(self._file)
        next_page = self._soup.find('a', {'class': 'next page-numbers'})
        if next_page is not None:
            res = requests.get(next_page.attrs['href'])
            res.raise_for_status()
            self._soup = bs4.BeautifulSoup(res.text, features="html.parser")
            self._loop_items(i)

    def _list_articles(self):
        self._loop_items()
        return self._articles
