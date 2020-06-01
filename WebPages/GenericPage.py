from Helpers.FileHelper import FileHelper


class GenericPage(object):
    title = ''

    def __init__(self):
        """

        :type _url: str
        """
        self._url = ''
        self._articleLink = ''
        self._header = ['url', 'date', 'title', 'text']
        self._file_helper = FileHelper()
        self._articles = self._file_helper.get_url(self._file)

    def _list_articles(self):
        pass

    def _loop_items(self):
        pass

    def save_articles(self):
        if not self._articles:
            self._file_helper.generate_header(self._file, self._header)
        self._loop_items()
        return self._articles
