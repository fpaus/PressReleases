from Helpers.FileHelper import FileHelper


def replace_new_line_and_tab(text: str) -> str:
    return text.strip().replace('\t', '').replace('\r', ' (newline) ').replace('\n', ' (newline) ').replace('”', '"').replace('“', '"')


class GenericArticle(object):
    def __init__(self, article_url: str, file_helper: FileHelper):
        self.date = None
        self.text = None
        self.title = None
        self.url = article_url
        self.fileHelper = file_helper
        self.soup = None

    def get_title(self):
        pass

    def get_date(self):
        pass

    def get_text(self):
        pass

    def save_article(self, file):
        self.fileHelper.append_data(file, [self.url, self.get_date(), self.get_title(), self.get_text()])
