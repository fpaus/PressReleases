#!/usr/bin/env python
from Scrapper import Scrapper
from WebPages.ChilePage import ChilePage
from WebPages.ColombiaPage import ColombiaPage
from WebPages.CubaPage import CubaPage
from WebPages.MexicoPage import MexicoPage
from WebPages.PanamaPage import PanamaPage
from WebPages.CostaRicaPage import CostaRicaPage
from WebPages.Selenium.SpainPage import SpainPage
from WebPages.PortugalPage import PortugalPage
from WebPages.ArgentinaPage import ArgentinaPage
from WebPages.BrazilPage import BrazilPage
from WebPages.UruguayPage import UruguayPage
from WebPages.Selenium.PeruPage import PeruPage
from WebPages.BoliviaPage import BoliviaPage
from WebPages.EcuadorPage import EcuadorPage

if __name__ == "__main__":
    scrapper = Scrapper(CubaPage())
    articles = scrapper.articles()
