class FileHelper(object):

    def __init__(self):
        pass

    def generateHeader(self, file, header):
        self.__saveLine(file, header)

    def appendData(self, file, data):
        self.__saveLine(file, data)

    def saveCsv(self, file, header, allData):
        with open(file, "wt", encoding="utf8") as f:
            line = "\t".join(header)
            f.write(line + "\n")
            for data in allData:
                line = "\t".join(data)
                f.write(line + "\n")

    def __saveLine(self, file, data: list):
        with open(file, "at", encoding="utf8") as f:
            line = "\t".join(data)
            f.write(line + "\n")
