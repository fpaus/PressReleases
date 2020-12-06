import os

from selenium import webdriver

from WebPages.Articles.PeruArticle import PeruArticle
from WebPages.PeruPage import PeruPage as Pp
import time


def send_keys(element, key_to_send):
    element.clear()
    element.send_keys(key_to_send)


class PeruPage(Pp):

    def __init__(self):
        super().__init__()
        self._driver = webdriver.Chrome()
        self._date_from_text = '01/01/2000'
        date_to = self._file_helper.get_last_date(self._file)
        self._date_to_text = date_to if date_to is not None else '18/04/2020'
        print(self._date_to_text)
        self._results_href_xpath = ""
        self._pagination_buttons_xpath = "/html/body/div[3]/div/div[2]/div/div/div/div/div[3]/div[2]/div/div/main/div/ul/li[@class='active']/a"
        self.page_number = 1

    def _loop_items(self):
        print('loop')
        self._driver.get(self._url)
        self._loop_pages()

    def _loop_pages(self):
        try:
            print(self.page_number)
            article_list = self._driver.find_elements_by_tag_name('article')
            article_links = [elem.get_attribute('href') for elem in
                             [a.find_element_by_tag_name('a') for a in article_list]]
            for url in article_links:
                if url not in self._articles:
                    print("_url:", url)
                    article = PeruArticle(url, self._file_helper)
                    article.save_article(self._file)
                    self._articles.append(url)
            next_page = self._driver.find_element_by_xpath(
                '/html/body/div[3]/div/div[2]/div/div/div/div/div[3]/div[2]/div/div/main/div/ul/li[7]/a')
            next_page.click()
            time.sleep(1)
            self.page_number = self.page_number + 1
            self._loop_pages()
        finally:
            self._driver.quit()
