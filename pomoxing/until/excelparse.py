import openpyxl
class ParseExcel:
    def readExcel(self,excelpath):
        self.workbook = openpyxl.load_workbook(excelpath)