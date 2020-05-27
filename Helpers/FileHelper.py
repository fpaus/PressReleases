from Helpers.ExcelHelper import ExcelHelper


class FileHelper(object):

    def __init__(self):
        self._excel_helper = ExcelHelper()

    def generate_header(self, file, header):
        self._save_line(file, header, self._excel_helper)

    def append_data(self, file, data):
        self._save_line(file, data, self._excel_helper)

    @staticmethod
    def _save_line(file, data: list, eh: ExcelHelper):
        csv_file = "{}.csv".format(file)
        with open(csv_file, "at", encoding="utf8") as f:
            line = "\t".join(data)
            f.write(line + "\n")
        eh.save_excel(data=data, filename=file)
        # eh.to_excel(_file)

    def get_url(self, file: str):
        try:
            return self._excel_helper.get_url(file)
        except:
            return []

    def get_last_date(self, file: str):
        print(file)
        try:
            return self._excel_helper.get_last_date(file)
        except:
            return None
