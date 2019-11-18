import openpyxl
class ParseExcel:
    def readExcel(self,excelPath):
        self.workbook=openpyxl.load_workbook(excelPath)
