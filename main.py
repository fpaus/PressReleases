#!/usr/bin/python
from Scrapper import Scrapper
from WebPages.SpainPage import SpainPage
from WebPages.ArgentinaPage import ArgentinaPage
from WebPages.BrazilPage import BrazilPage

if __name__ == "__main__":
    scrapper = Scrapper(SpainPage())
    articles = scrapper.articles()
