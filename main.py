from Scrapper import Scrapper
from WebPages.SpainPage import SpainPage

if __name__ == "__main__":
    scrapper = Scrapper(SpainPage())
    articles = scrapper.articles()
