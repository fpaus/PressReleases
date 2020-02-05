from Scrapper import Scrapper
from WebPages.ArgentinaPage import ArgentinaPage

if __name__ == "__main__":
    scrapper = Scrapper(ArgentinaPage())
    articles = scrapper.articles()
    for article in articles:
        print(article)
