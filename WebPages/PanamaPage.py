import bs4
import requests

from WebPages.Articles.PanamaArticle import PanamaArticle
from WebPages.GenericPage import GenericPage


class PanamaPage(GenericPage):
    def __init__(self):
        self._file = 'Panama'
        super().__init__()
        self._root_url = 'https://minrel.gob.cl'
        self._url = 'https://mire.gob.pa/noticias/todas-las-noticias/page/{}/'
        # res = requests.get(self._url)
        # res.raise_for_status()
        # self._soup = bs4.BeautifulSoup(res.text, features="html.parser")
        self._article_link = '.fusion-post-content-wrapper'

    def _loop_items(self, i=1):
        print(i)
        res = requests.get(self._url.format(i))
        res.raise_for_status()
        self._soup = bs4.BeautifulSoup(res.text, features="html.parser")
        arts = self._soup.select(self._article_link)
        if len(arts) > 0:
            for art in arts:
                article_url = art.find('a').attrs['href']
                title = art.find('a').getText()
                url = article_url
                print(url)
                if url not in self._articles:
                    article = PanamaArticle(url, self._file_helper)
                    article.save_article(self._file)
                    self._articles.append(url)
                    print(title)
            i = i + 1
            self._loop_items(i)

    def _list_articles(self):
        self._loop_items()
        return self._articles


