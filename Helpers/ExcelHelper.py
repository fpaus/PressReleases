import pandas as pd


class ExcelHelper(object):
    def __init__(self):
        pass

    def to_excel(self, filename: str):
        xlsx_filename = '{}.xlsx'.format(filename)
        csv_filename = '{}.csv'.format(filename)
        read_file = pd.read_csv(csv_filename, sep='\t')
        read_file.to_excel(xlsx_filename, index=None, header=True)

    def get_url(self, filename: str):
        xlsx_filename = '{}.xlsx'.format(filename)
        df = pd.DataFrame(pd.read_excel(xlsx_filename))
        l = []
        for url in df['url']:
            l.append(url)
        return l
