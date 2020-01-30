from WebPages.GenericPage import GenericPage


class Scrapper(object):
    def __init__(self, page: GenericPage):
        """
        :type page: GenericPage
        """
        self.page = page
