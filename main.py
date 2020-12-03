#!/usr/bin/env python
import importlib
import sys
from Scrapper import Scrapper

if __name__ == "__main__":
    country = ''
    if len(sys.argv) == 2:
        country = sys.argv[1].capitalize()
    else:
        from os import listdir
        from os.path import isfile, join
        [print(f[:-7]) for f in listdir('WebPages') if (isfile(join('WebPages', f)) and f != 'GenericPage.py')]
        country = input('enter country: ').capitalize()
    PageClass = getattr(importlib.import_module(f"WebPages.{country}Page"), f"{country}Page")
    print(f'scrapping{country}')
    scrapper = Scrapper(PageClass())
    articles = scrapper.articles()
