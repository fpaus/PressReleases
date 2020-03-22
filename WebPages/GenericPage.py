from Helpers.FileHelper import FileHelper

class GenericPage(object):
    title = ''

    def __init__(self):
        """

        :type url: str
        """
        self.url = ''
        self.articleLink = ''
        self.header = ['url', 'date', 'title', 'text']
        self.fileHelper = FileHelper()
        self.articles = self.fileHelper.get_url(self.file)

    def list_articles(self):
        pass

    def save_articles(self):
        if self.articles == []:
            self.fileHelper.generate_header(self.file, self.header)
        self.loop_items()
        return self.articles    
