import xlrd
import os
import readconfig

class ReadExcel:
    def __init__(self,filename,sheetname):
        self.filename = filename
        self.sheetname = sheetname
        # 获取测试文件的路径
        testdata_path = os.path.join(readconfig.proDir,"testdata",filename)
        # 打开测试文件
        exceldata = xlrd.open_workbook(testdata_path)
        # 获取sheet
        self.tables = exceldata.sheet_by_name(sheetname)

    def get_testdata(self):
        # 获取行数
        rows = self.tables.nrows
        # 获取列名
        columns_name = self.tables.row_values(0)
        casedatalist = []
        # 循环读取数据，从第二行开始读取
        for rownum in range(1,rows):
            # 每一行数据存储在字典中
            casedir = {}
            for column in range(0,len(columns_name)):
                casedir[columns_name[column]] = self.tables.cell_value(rownum,column)
            # 将每一行数据存储在casedatalist中
            casedatalist.append(casedir)
        return casedatalist

    def get_caselist(self):
        # 获取行数
        rows = self.tables.nrows
        # 获取列名
        columns_name = self.tables.row_values(0)
        casedatalist = []
        # 循环读取数据，从第二行开始读取
        for rownum in range(1,rows):
            # 每一行数据存储在字典中
            cases = []
            for column in range(0, len(columns_name)):
                cases.append(self.tables.cell_value(rownum, column))
            # 将每一行数据存储在casedatalist中
            rows_values = tuple(cases)
            casedatalist.append(rows_values)
        return casedatalist


if __name__ == "__main__":
    readexcel = ReadExcel("LoginData.xlsx","Sheet1")
    readexcel.get_caselist()
