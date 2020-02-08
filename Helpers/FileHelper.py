class FileHelper(object):

    def __init__(self):
        pass

    def generate_header(self, file, header):
        self.__save_line__(file, header)

    def append_data(self, file, data):
        self.__save_line__(file, data)

    @staticmethod
    def save_csv(file, header, all_data):
        with open(file, "wt", encoding="utf8") as f:
            line = "\t".join(header)
            f.write(line + "\n")
            for data in all_data:
                line = "\t".join(data)
                f.write(line + "\n")

    @staticmethod
    def __save_line__(file, data: list):
        with open(file, "at", encoding="utf8") as f:
            line = "\t".join(data)
            f.write(line + "\n")
