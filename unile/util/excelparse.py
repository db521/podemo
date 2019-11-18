#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/30 16:56 
# @File : excelparse.py 
import openpyxl
class ParseExcel:
    def readExcel(self,excelpath):
        self.workbook=openpyxl.load_workbook(excelpath)