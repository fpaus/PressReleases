import os

from selenium import webdriver

from WebPages.Articles.SpainArticle import SpainArticle
from WebPages.SpainPage import SpainPage as Sp


def send_keys(element, key_to_send):
    element.clear()
    element.send_keys(key_to_send)


class SpainPage(Sp):

    def __init__(self):
        super().__init__()
        self._driver = webdriver.Chrome()
        self._date_from_text = '01/01/2000'
        date_to = self._file_helper.get_last_date(self._file)
        self._date_to_text = date_to if date_to is not None else '18/04/2020'
        print(self._date_to_text)
        self._results_href_xpath = "//div[@class='buscadorResultados']/div/ul/li/div/div/a"
        self._pagination_buttons_xpath = '//*[@id="ctl00_SPWebPartManager1_g_05c9fa53_6e44_444a_8ed7_a152a2ee7ae7_ctl00_pagerResultados"]'

    def _loop_items(self):
        print('loop')
        self._driver.get(self._url)
        date_from = self._driver.find_element_by_xpath(
            '//*[@id="ctl00_SPWebPartManager1_g_05c9fa53_6e44_444a_8ed7_a152a2ee7ae7_ctl00_dtDesde_dtDesdeDate"]')
        date_to = self._driver.find_element_by_xpath(
            '//*[@id="ctl00_SPWebPartManager1_g_05c9fa53_6e44_444a_8ed7_a152a2ee7ae7_ctl00_dtHasta_dtHastaDate"]')
        seach_button = self._driver.find_element_by_xpath(
            '//*[@id="ctl00_SPWebPartManager1_g_05c9fa53_6e44_444a_8ed7_a152a2ee7ae7_ctl00_btnBuscar"]')
        send_keys(date_from, self._date_from_text)
        send_keys(date_to, self._date_to_text)
        print("fechas")
        seach_button.click()
        print("busqueda")
        self._loop_pages()

    def _loop_pages(self):
        try:
            actual_page = int(self._driver.find_element_by_xpath(self._pagination_buttons_xpath + '/span')._text)
            print("page:", actual_page)
            link_list = self._driver.find_elements_by_xpath(self._results_href_xpath)
            page_articles = [elem.get_attribute('href') for elem in link_list]
            # print("urls:", len(page_articles))
            # self._articles = self._articles + page_articles
            for url in page_articles:
                if url not in self._articles:
                    print("_url:", url)
                    article = SpainArticle(url, self._file_helper)
                    article.save_article(self._file)
                    self._articles.append(url)
            pagination = self._driver.find_elements_by_xpath(self._pagination_buttons_xpath + "/input")
            # print(self._articles)
            next_page = pagination[0]
            for index, page in enumerate(pagination):
                page_text = page.get_attribute('value')
                if page_text != '...':
                    if int(page.get_attribute('value')) > actual_page:
                        next_page = page
                        break
                    elif int(page.get_attribute('value')) == 100:
                        self._date_to_text = self._file_helper.get_last_date(self._file)  # '12/06/2015' #'18/04/2020'
                        self._loop_items()
                elif index > 0:
                    next_page = page
                    break
            next_page.click()
            self._loop_pages()
        finally:
            self._driver.quit()
