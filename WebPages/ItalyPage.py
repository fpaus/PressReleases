import bs4
import requests
import warnings

from WebPages.Articles.ItalyArticle import ItalyArticle
from WebPages.GenericPage import GenericPage


# 575126091

class ItalyPage(GenericPage):
    def __init__(self):
        warnings.filterwarnings("ignore")
        self._file = 'Italy'
        super().__init__()
        self._root_url = 'https://www.esteri.it'
        self._url = 'https://www.esteri.it/mae/en/sala_stampa/archivionotizie/comunicati/'
        res = requests.get(self._url, verify=False)
        res.raise_for_status()
        self._soup = bs4.BeautifulSoup(res.text, features="html.parser")
        self._article_link = '.desc_lista'
        self._next_page = ''
        self._next = {'title': 'Forward'}

    def _loop_items(self):
        warnings.filterwarnings("ignore")
        arts = self._soup.select(self._article_link)
        if len(arts) > 0:
            for art in arts:
                partial_url = art.find('a').attrs['href']
                url = self._root_url + partial_url
                if url not in self._articles:
                    print('processing:', url)
                    article = ItalyArticle(url, self._file_helper)
                    article.save_article(self._file)
                    self._articles.append(url)
                    print(article._get_date())
            self._next_page = self._soup.find('a', self._next).attrs['href']
            # self._soup.select(self._next)[0].select('a')[0].attrs['href']
            print('next page:', self._next_page)
            res = requests.get(self._next_page, verify=False)
            res.raise_for_status()
            self._soup = bs4.BeautifulSoup(res.text, features="html.parser")
            self._loop_items()

    def _list_articles(self):
        self._loop_items()
        return self._articles
