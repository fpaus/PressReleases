from Helpers.ExcelHelper import ExcelHelper


class FileHelper(object):

    def __init__(self):
        self.eh = ExcelHelper()

    def generate_header(self, file, header):
        self.__save_line__(file, header, self.eh)

    def append_data(self, file, data):
        self.__save_line__(file, data, self.eh)

    #@staticmethod
    def save_csv(file, header, all_data):
        csv_file = "{}.csv".format(file)
        with open(csv_file, "wt", encoding="utf8") as f:
            line = "\t".join(header)
            f.write(line + "\n")
            for data in all_data:
                line = "\t".join(data)
                f.write(line + "\n")

    @staticmethod
    def __save_line__(file, data: list, eh: ExcelHelper):
        csv_file = "{}.csv".format(file)
        with open(csv_file, "at", encoding="utf8") as f:
            line = "\t".join(data)
            f.write(line + "\n")
        eh.to_excel(file)

    def get_url(self, file: str):
        try:
            return self.eh.get_url(file)
        except :
          return []
