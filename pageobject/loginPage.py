#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/30 17:01 
# @File : loginPage.py
import json
from util.wait import getElementImplicitWait as ge
from selenium import webdriver
class login:
    def __init__(self, driver):
        self.driver = driver

    def nameObj(self):  # 单个元素的获取方法
        try:
            with open('../config/pageobject.json','r',encoding='utf-8') as f:
                sw= json.loads(f.read())
            ss = sw["login"]["name"]
            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)

            return elemetObj
        except Exception as e:
            raise e

    def passwdObj(self):  # 单个元素的获取方法
        try:
            with open('../config/pageobject.json', 'r', encoding='utf-8') as f:
                sw = json.loads(f.read())
            ss = sw["login"]["passwd"]
            locatetype = ss[0]
            locatorExpression = ss[1]
            # print(22222222)
            # print(locatetype,locatorExpression)
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e

    def btnObj(self):  # 单个元素的获取方法
        try:
            with open('../config/pageobject.json', 'r', encoding='utf-8') as f:
                sw = json.loads(f.read())
            ss = sw["login"]["btn"]
            locatetype = ss[0]
            locatorExpression = ss[1]
            print(333333)
            print(locatetype,locatorExpression)
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e

    def zuzhiObj(self):  # 单个元素的获取方法
        try:
            with open('../config/pageobject.json', 'r', encoding='utf-8') as f:
                sw = json.loads(f.read())
            ss = sw["login"]["zuzhi"]
            locatetype = ss[0]
            locatorExpression = ss[1]
            # print(333333)
            print(locatetype,locatorExpression)
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e
    def addObj(self):  # 单个元素的获取方法
        try:
            with open('../config/pageobject.json', 'r', encoding='utf-8') as f:
                sw = json.loads(f.read())
            ss = sw["login"]["add"]
            locatetype = ss[0]
            locatorExpression = ss[1]
            # print(333333)
            # print(locatetype,locatorExpression)
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e

if __name__ == '__main__':
    driver=webdriver.Chrome()
    logins=login(driver)
    logins.nameObj()

