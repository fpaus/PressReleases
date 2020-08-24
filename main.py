#!/usr/bin/env python
from Scrapper import Scrapper
from WebPages.ChilePage import ChilePage
from WebPages.ColombiaPage import ColombiaPage
from WebPages.Selenium.SpainPage import SpainPage
from WebPages.PortugalPage import PortugalPage
from WebPages.ArgentinaPage import ArgentinaPage
from WebPages.BrazilPage import BrazilPage
from WebPages.UruguayPage import UruguayPage
from WebPages.Selenium.PeruPage import PeruPage

if __name__ == "__main__":
    scrapper = Scrapper(PeruPage())
    articles = scrapper.articles()
