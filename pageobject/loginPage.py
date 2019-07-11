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
            with open('../config/pageobject.json',mode='r') as f:
                ss = json.loads(f.read())
            name = ss["login"]["len"]
            locatetype = name[0]
            locatorExpression = name[1]
            print(locatetype)
            print(locatorExpression)
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e


    def nameObj1(self):  # 单个元素的获取方法
        try:
            with open('../config/pageobject.json',mode='r') as f:
                ss = json.loads(f.read())
                print(ss)
            name = ss["login"]["name"]
            locatetype = name[0]
            locatorExpression = name[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e


    def passwdObj(self):  # 单个元素的获取方法
        try:
            with open('../config/pageobject.json',mode='r') as f:
                bb = json.loads(f.read())
            passwd = bb["login"]["passwd"]
            locatetype = passwd[0]
            locatorExpression = passwd[1]
            # ss = json.loads('./config/pageobject.json')["login"]["passwd"]
            # locatetype = ss[0]
            # locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e

    def urlObj(self):  # 单个元素的获取方法
        try:
            with open('../config/config.json', mode='r') as f:
                ww = json.loads(f.read())
                url = ww['url']
            return url
        except Exception as e:
            raise e


    def urlObj1(self):  # 单个元素的获取方法
        try:
            with open('../config/passwd.json', mode='r') as a:
                zz = json.loads(a.read())
            user = zz["login1"]["user"]
            return user
        except Exception as e:
            raise e


    def urlObj2(self):  # 单个元素的获取方法
        try:
            with open('../config/passwd.json', mode='r') as a:
                zz = json.loads(a.read())
            passwd = zz["login1"]["passwd"]
            return passwd
        except Exception as e:
            raise e


# if __name__ == '__main__':
#     from selenium import  webdriver
#     dri = webdriver.Chrome()
#     log = login(dri)
#     log.nameObj()
#     log.nameObj1()
#     log.passwdObj()
