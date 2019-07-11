#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/30 17:01 
# @File : loginPage.py
import json
from util.wait import getElementImplicitWait as ge


class login:
    def __init__(self, driver):
        self.driver = driver

    def nameObj(self):  # 单个元素的获取方法
        try:
            with open("../config/pageobject.json", 'r')as f:
                ss = json.loads(f.read())["login"]["name"]
                locatetype = ss[0]
                locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e

    def passwdObj(self):  # 单个元素的获取方法
        try:
            with open("../config/pageobject.json", 'r')as f:
                ss = json.loads(f.read())["login"]["passwd"]
                locatetype = ss[0]
                locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e

    def btnObj(self):
        try:
            with open("../config/pageobject.json", 'r')as f:
                ss = json.loads(f.read())["login"]["button"]
                btn_id = ss[0]
                btn_vau = ss[1]
            # print(btn_id, btn_vau)
            elemetObj = ge(self.driver, btn_id, btn_vau)
            return elemetObj
        except Exception as e:
            raise e

    def zuzhiObj(self):
        try:
            with open("../config/pageobject.json", 'r')as f:
                ss = json.loads(f.read())["login"]["zuzhi"]
                zuzhi0 = ss[0]
                zuzhi1 = ss[1]
            # print(zuzhi0, zuzhi1)
            elemetObj = ge(self.driver, zuzhi0, zuzhi1)
            return elemetObj
        except Exception as e:
            raise e

    def zuzhiwhObj(self):
        try:
            with open("../config/pageobject.json", 'r')as f:
                ss = json.loads(f.read())["login"]["bumen"]
                bumen0 = ss[0]
                bumen1 = ss[1]
            # print(bumen0, bumen1)
            elemetObj = ge(self.driver, bumen0, bumen1)
            return elemetObj
        except Exception as e:
            raise e

    def deptnameObj(self):
        try:
            with open("../config/pageobject.json", 'r')as f:
                ss = json.loads(f.read())["login"]["dept_name"]
                dept_name0 = ss[0]
                dept_name1 = ss[1]
            # print(dept_name0, dept_name1)
            elemetObj = ge(self.driver, dept_name0, dept_name1)
            return elemetObj
        except Exception as e:
            raise e

    def deptlistObj(self):
        try:
            with open("../config/pageobject.json", 'r')as f:
                ss = json.loads(f.read())["login"]["dept_list"]
                dept_list0 = ss[0]
                dept_list1 = ss[1]
            elemetObj = ge(self.driver, dept_list0, dept_list1)
            return elemetObj
        except Exception as e:
            raise e

    def deptbtnObj(self):
        try:
            with open("../config/pageobject.json", 'r')as f:
                ss = json.loads(f.read())["login"]["dept_btn"]
                dept_btn0 = ss[0]
                dept_btn1 = ss[1]
            elemetObj = ge(self.driver, dept_btn0, dept_btn1)
            return elemetObj
        except Exception as e:
            raise e
# if __name__ == '__main__':
# from selenium import webdriver
# bro = webdriver.Chrome()
# aa = login(bro)
# aa.btnObj()
