#!/usr/bin/env python
from Scrapper import Scrapper
from WebPages.Selenium.SpainPage import SpainPage
from WebPages.PortugalPage import PortugalPage
from WebPages.ArgentinaPage import ArgentinaPage
from WebPages.BrazilPage import BrazilPage
from WebPages.UruguayPage import UruguayPage

if __name__ == "__main__":
    scrapper = Scrapper(UruguayPage())
    articles = scrapper.articles()
