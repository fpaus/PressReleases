import bs4
import requests

from WebPages.Articles.UruguayArticle import UruguayArticle
from WebPages.GenericPage import GenericPage


class UruguayPage(GenericPage):
    def __init__(self):
        self._file = 'Uruguay'
        super().__init__()
        self._root_url = 'https://www.gub.uy'
        self._url = 'https://www.gub.uy/ministerio-relaciones-exteriores/comunicacion/comunicados?field_tematica_target_id=All&field_publico_target_id=All&year=all&month=all&page=0'
        res = requests.get(self._url)
        res.raise_for_status()
        self._soup = bs4.BeautifulSoup(res.text, features="html.parser")
        self._article_link = '.Media-body h3'
        self._next_page = '&page='

    def _loop_items(self, i=1):
        print(i)
        arts = self._soup.select(self._article_link)
        if len(arts) > 0:
            for art in arts:
                partial_url = art.find('a').attrs['href']
                url = self._root_url + partial_url
                if url not in self._articles:
                    self._articles.append(url)
                    article = UruguayArticle(url, self._file_helper)
                    article.save_article(self._file)
                    print(article._get_date())
            res = requests.get('{}{}{}'.format(self._url, self._next_page, i))
            res.raise_for_status()
            self._soup = bs4.BeautifulSoup(res.text, features="html.parser")
            i = i + 1
            self._loop_items(i)

    def _list_articles(self):
        self._loop_items()
        return self._articles


