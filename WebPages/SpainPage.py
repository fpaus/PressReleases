from datetime import date
from datetime import timedelta

from Helpers.FileHelper import FileHelper
from WebPages.Articles.SpainArticle import SpainArticle
from WebPages.GenericPage import GenericPage


class SpainPage(GenericPage):
    def __init__(self):
        super().__init__()
        self.rootURL = 'http://www.exteriores.gob.es/Portal/es/SalaDePrensa'
        # self.url = 'http://www.exteriores.gob.es/Portal/es/SalaDePrensa'
        self.articles = []
        self.file = 'Spain.csv'
        self.fileHelper = FileHelper()
        self.maxFormerFormat = 553
        self.partialFormerUrl = '/NotasDePrensa/Paginas/Articulos/Comunicado{}.aspx'
        self.FistNewFormat = date(2013, 3, 30)
        self.partialNewUrl = '/Comunicados/Paginas/{}_COMUNICADOS/{}_COMU{}.aspx'

    def loop_items(self):
        for comu in range(1, self.maxFormerFormat + 1):
            url = self.rootURL + self.partialFormerUrl.format(comu)
            try:
                article = SpainArticle(url, self.fileHelper)
                article.save_article(self.file)
                print(article.get_date())
                self.articles.append(url)
            except Exception as e:
                print(e)
                print(e.with_traceback())
                print("error in {}".format(url))
        for comu in range(1, 500):
            year = 2013
            while year == self.FistNewFormat.year:
                article_date = '{}{:02d}{:02d}'.format(self.FistNewFormat.year, self.FistNewFormat.month,
                                                       self.FistNewFormat.day)
                try:
                    url = self.rootURL + self.partialNewUrl.format(year, article_date, comu)
                    article = SpainArticle(url, self.fileHelper)
                    article.save_article(self.file)
                    print(article.get_date())
                    self.articles.append(url)
                    self.FistNewFormat = self.FistNewFormat + timedelta(days=1)
                except:
                    self.FistNewFormat = self.FistNewFormat + timedelta(days=1)
        for year in range(2014, 2021):
            exist_articles = True
            comu = 1
            self.FistNewFormat = date(2014, 1, 1)
            while exist_articles:
                article_date = '{}{:02d}{:02d}'.format(self.FistNewFormat.year, self.FistNewFormat.month,
                                                       self.FistNewFormat.day)
                try:
                    url = self.rootURL + self.partialNewUrl.format(year, article_date, comu)
                    article = SpainArticle(url, self.fileHelper)
                    article.save_article(self.file)
                    print(article.get_date())
                    self.articles.append(url)
                    print(comu)
                    comu = comu + 1
                except:
                    try:
                        print(url)
                        com = '{:03d}'.format(comu)
                        url = self.rootURL + self.partialNewUrl.format(year, article_date, com)
                        article = SpainArticle(url, self.fileHelper)
                        article.save_article(self.file)
                        print(article.get_date())
                        self.articles.append(url)
                        print(comu)
                        comu = comu + 1
                    except:
                        self.FistNewFormat = self.FistNewFormat + timedelta(days=1)
                        print(url)
                        exist_articles = self.FistNewFormat.year == year

    def list_articles(self):
        self.loop_items()
        return self.articles

    def save_articles(self):
        self.fileHelper.generate_header(self.file, self.header)
        self.loop_items()
        return self.articles