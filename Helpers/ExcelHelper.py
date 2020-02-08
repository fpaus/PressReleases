import pandas as pd


class ExcelHelper(object):
    def __init__(self):
        pass

    def to_excel(self, csv_filename: str):
        xlsx_filename = '{}.xlsx'.format(csv_filename.split('.')[0])
        read_file = pd.read_csv(csv_filename, sep='\t')
        read_file.to_excel(xlsx_filename, index=None, header=True)
