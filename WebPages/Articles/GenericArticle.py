from Helpers.FileHelper import FileHelper


def replace_new_line_and_tab(text: str) -> str:
    return text.strip().replace('\t', '').replace('\r', ' (newline) ').replace('\n', ' (newline) ').replace('”', '"').replace('“', '"')


class GenericArticle(object):
    def __init__(self, article_url: str, file_helper: FileHelper):
        self._date = None
        self._text = None
        self._title = None
        self._url = article_url
        self._file_helper = file_helper
        self._soup = None

    def _get_title(self):
        pass

    def _get_date(self):
        pass

    def _get_text(self):
        pass

    def save_article(self, file):
        self._file_helper.append_data(file, [self._url, self._get_date(), self._get_title(), self._get_text()])
