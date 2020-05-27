from WebPages.GenericPage import GenericPage


class Scrapper(object):
    _page: GenericPage

    def __init__(self, page: GenericPage):
        """
        :type page: GenericPage
        """
        self._page = page

    def search_multiple(self):
        pass

    def articles(self):
        return self._page.save_articles()
