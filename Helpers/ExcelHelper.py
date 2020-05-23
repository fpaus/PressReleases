import pandas as pd
import os.path


class ExcelHelper(object):
    def __init__(self):
        pass

    def to_excel(self, filename: str):
        xlsx_filename = '{}.xlsx'.format(filename)
        csv_filename = '{}.csv'.format(filename)
        read_file = pd.read_csv(csv_filename, sep='\t')
        read_file.to_excel(xlsx_filename, index=None, header=True)

    def save_excel(self, data, filename: str):
        xlsx_filename = '{}.xlsx'.format(filename)
        if not os.path.isfile(xlsx_filename):
            self.__create_excel__(xlsx_filename)
        df = pd.DataFrame(pd.read_excel(xlsx_filename))
        df.loc[len(df)] = data
        df.to_excel(xlsx_filename, index=None, header=True)

    def __create_excel__(self, xlsx_filename):
        df = pd.DataFrame(columns=['url', 'date', 'title', 'text'])
        df.to_excel(xlsx_filename, index=None, header=True)

    def get_url(self, filename: str):
        xlsx_filename = '{}.xlsx'.format(filename)
        df = pd.DataFrame(pd.read_excel(xlsx_filename))
        l = []
        for url in df['url']:
            l.append(url)
        return l

    def get_last_date(self, filename: str):
        xlsx_filename = '{}.xlsx'.format(filename)
        print(xlsx_filename)
        df = pd.DataFrame(pd.read_excel(xlsx_filename))
        date = df['date'][len(df['date']) - 1]
        return date
