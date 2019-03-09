import xlrd


class ReadExcel:
    def __init__(self, filename, sheetid):
        self.filename = filename
        self.sheetid = sheetid
        self.tables = self.get_data()

    def get_data(self):
        data = xlrd.open_workbook(self.filename)
        tables = data.sheets()[self.sheetid]
        return tables