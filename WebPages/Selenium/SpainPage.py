from datetime import date
from datetime import timedelta
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Helpers.FileHelper import FileHelper
from WebPages.Articles.SpainArticle import SpainArticle
from WebPages.SpainPage import SpainPage as sp
import os

class SpainPage(sp):

    def __init__(self):
        print(os.getcwd())
        super().__init__()
        self.driver = webdriver.Chrome()
        print('firefox')
        self.date_from_text = '01/01/2000'
        self.date_to_text = '18/04/2020'
        self.results_href_xpath = "//div[@class='buscadorResultados']/div/ul/li/div/div/a"
        self.pagination_buttons_xpath = '//*[@id="ctl00_SPWebPartManager1_g_05c9fa53_6e44_444a_8ed7_a152a2ee7ae7_ctl00_pagerResultados"]'

    def loop_items(self):
        print('loop')
        self.driver.get(self.url)
        date_from = self.driver.find_element_by_xpath('//*[@id="ctl00_SPWebPartManager1_g_05c9fa53_6e44_444a_8ed7_a152a2ee7ae7_ctl00_dtDesde_dtDesdeDate"]')
        date_to = self.driver.find_element_by_xpath('//*[@id="ctl00_SPWebPartManager1_g_05c9fa53_6e44_444a_8ed7_a152a2ee7ae7_ctl00_dtHasta_dtHastaDate"]')
        seach_button = self.driver.find_element_by_xpath('//*[@id="ctl00_SPWebPartManager1_g_05c9fa53_6e44_444a_8ed7_a152a2ee7ae7_ctl00_btnBuscar"]')
        self.send_keys(date_from, self.date_from_text)
        self.send_keys(date_to, self.date_to_text)
        print("fechas")
        seach_button.click()
        print("busqueda")
        self.loop_pages()

    def loop_pages(self):
        try:
            actual_page = int(self.driver.find_element_by_xpath(self.pagination_buttons_xpath + '/span').text)
            link_list = self.driver.find_elements_by_xpath(self.results_href_xpath)
            page_articles = [elem.get_attribute('href') for elem in link_list]
            print("urls:", len(page_articles))
            #self.articles = self.articles + page_articles
            for url in page_articles:
                if url not in self.articles:
                    article = SpainArticle(url, self.fileHelper)
                    article.save_article(self.file)
                    self.articles.append(url)
            pagination = self.driver.find_elements_by_xpath(self.pagination_buttons_xpath + "/input")
            print(self.articles)
            next_page = pagination[0]
            for page in pagination:
                print(page.get_attribute('value'))
                if int(page.get_attribute('value')) > actual_page:
                    next_page = page
                    break
            next_page.click()
            self.loop_pages()
        finally:
            self.driver.quit()

    def send_keys(self, element, key_to_send):
        element.clear()
        element.send_keys(key_to_send)