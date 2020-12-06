import bs4
import requests

from WebPages.Articles.ColombiaArticle import ColombiaArticle
from WebPages.GenericPage import GenericPage


class ColombiaPage(GenericPage):
    def __init__(self):
        self._file = 'Colombia'
        super().__init__()
        self._root_url = 'https://www.cancilleria.gov.co'
        self._url = 'https://www.cancilleria.gov.co/newsroom/publiques'
        self._article_link = '.view-content a'
        self._next_page = '?page='

    def _loop_items(self, i=0):
        res = requests.get(f'{self.url}{self.next_page}{i}')  ##('{}{}{}'.format(self._url, self._next_page, i))
        res.raise_for_status()
        self._soup = bs4.BeautifulSoup(res.text, features="html.parser")
        print(i)
        arts = self._soup.select(self._article_link)
        if len(arts) > 0:
            for art in arts:
                partial_url = art.attrs['href']
                if partial_url[0] == '/':
                    title = art.text
                    url = self._root_url + partial_url
                    if url not in self._articles:
                        print(title)
                        self._articles.append(url)
                        article = ColombiaArticle(url, self._file_helper)
                        article.save_article(self._file)
            i = i + 1
            self._loop_items(i)

    def _list_articles(self):
        self._loop_items()
        return self._articles
