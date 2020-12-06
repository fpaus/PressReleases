import bs4
import requests
import warnings

from WebPages.Articles.ObamaArticle import ObamaArticle
from WebPages.GenericPage import GenericPage


class ObamaPage(GenericPage):
    def __init__(self):
        warnings.filterwarnings("ignore")
        self._file = 'Obama'
        super().__init__()
        self._root_url = 'https://2009-2017.state.gov'
        self._url = 'https://2009-2017.state.gov/r/pa/prs/ps/index.htm'
        res = requests.get(self._url, verify=False)
        res.raise_for_status()
        self._soup = bs4.BeautifulSoup(res.text, features="html.parser")
        self._article_link = '.desc_lista'
        self._next_page = ''
        self._next = {'title': 'Forward'}

    def _loop_items(self):
        warnings.filterwarnings("ignore")
        menu = self._soup.find('ul', {'class': 'menu'})
        years_urls = [y.attrs['href'] for y in menu.find_all('a') if y.attrs['href'][0] == '/']
        for year in years_urls:
            res = requests.get(f'https:{year}', verify=False)
            res.raise_for_status()
            print(year)
            self._soup = bs4.BeautifulSoup(res.text, features="html.parser")
            menu = self._soup.find('ul', {'class': 'menu'})
            months_url = [y.attrs['href'] for y in menu.find_all('a') if y.attrs['href'][0] == '/']
            for month in months_url:
                res = requests.get(f'https:{month}', verify=False)
                res.raise_for_status()
                print(f'{year}-{month}')
                self._soup = bs4.BeautifulSoup(res.text, features="html.parser")
                table_links = [a for a in self._soup.find('div', {'class': 'l-wrap'}).find_all('a')]
                for partial_url in table_links:
                    url = f'{self._root_url}{partial_url.attrs["href"]}'
                    if url not in self._articles:
                        article = ObamaArticle(url, self._file_helper, partial_url.getText())
                        article.save_article(self._file)
                        self._articles.append(url)

    def _list_articles(self):
        self._loop_items()
        return self._articles
