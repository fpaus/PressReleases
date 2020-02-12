class GenericPage(object):
    title = ''

    def __init__(self):
        """

        :type url: str
        """
        self.url = ''
        self.articleLink = ''
        self.header = ['url', 'date', 'title', 'text']
    def list_articles(self):
        pass

    def save_articles(self):
        pass
