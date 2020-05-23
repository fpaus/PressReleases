#!/usr/bin/env python
from Scrapper import Scrapper
from WebPages.Selenium.SpainPage import SpainPage
from WebPages.PortugalPage import PortugalPage
from WebPages.ArgentinaPage import ArgentinaPage
from WebPages.BrazilPage import BrazilPage

if __name__ == "__main__":
    scrapper = Scrapper(PortugalPage())
    articles = scrapper.articles()
