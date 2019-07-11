#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/30 17:01 
# @File : loginPage.py
import json
from util.wait import getElementImplicitWait as ge


class login:
    def __init__(self, driver):
        self.driver = driver

    def buttonObj(self):  # 单个元素的获取方法
        try:
            with open('../config/pageobject.json', mode='r')as f:
                ss = json.loads(f.read())
                # print(ss)
            name = ss["login"]["loginbtn"]
            # print(name)
            locatetype = name[0]
            # print(locatetype)
            locatorExpression = name[1]
            # print(locatorExpression)
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e

    def userObj(self):  # 单个元素的获取方法
        try:
            with open('../config/pageobject.json', mode='r')as f:
                ss = json.loads(f.read())
                # print(ss)
            user = ss["login"]["account"]
            # print(user)
            locatetype = user[0]
            # print(locatetype)
            locatorExpression = user[1]
            # print(locatorExpression)
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e

    def pwdObj(self):  # 单个元素的获取方法
        try:
            with open('../config/pageobject.json', mode='r')as f:
                ss = json.loads(f.read())
                # print(ss)
            pwd = ss["login"]["password"]
            # print(pwd)
            locatetype = pwd[0]
            # print(locatetype)
            locatorExpression = pwd[1]
            # print(locatorExpression)
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e

    def loginsObj(self):  # 单个元素的获取方法
        try:
            with open('../config/pageobject.json', mode='r')as f:
                ss = json.loads(f.read())
                print(ss)
            pwd = ss["login"]["logins"]
            print(pwd)
            locatetype = pwd[0]
            print(locatetype)
            locatorExpression = pwd[1]
            print(locatorExpression)
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e


# if __name__ == '__main__':
#     from selenium import webdriver
#
#     dd = webdriver.Chrome()
#     asd = login(dd)
#     # asd.buttonObj()
#     # asd.userObj()
#     asd.pwdObj()
