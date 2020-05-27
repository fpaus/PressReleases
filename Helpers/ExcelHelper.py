import pandas as pd
import os.path


class ExcelHelper(object):
    def __init__(self):
        pass

    def save_excel(self, data, filename: str):
        xlsx_filename = '{}.xlsx'.format(filename)
        if not os.path.isfile(xlsx_filename):
            self._create_excel(xlsx_filename)
        df = pd.DataFrame(pd.read_excel(xlsx_filename))
        df.loc[len(df)] = data
        df.to_excel(xlsx_filename, index=None, header=True)

    def _create_excel(self, xlsx_filename):
        df = pd.DataFrame(columns=['_url', 'date', 'title', 'text'])
        df.to_excel(xlsx_filename, index=None, header=True)

    def get_url(self, filename: str):
        xlsx_filename = '{}.xlsx'.format(filename)
        df = pd.DataFrame(pd.read_excel(xlsx_filename))
        l = []
        for url in df['_url']:
            l.append(url)
        return l

    def get_last_date(self, filename: str):
        xlsx_filename = '{}.xlsx'.format(filename)
        print(xlsx_filename)
        df = pd.DataFrame(pd.read_excel(xlsx_filename))
        date = df['date'][len(df['date']) - 1]
        return date
