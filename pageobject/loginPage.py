#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/30 17:01 
# @File : loginPage.py
import json
from util.wait import getElementImplicitWait as ge


class login:
    def __init__(self, driver):
        self.driver = driver

    def elemObj(self):
        try:
            with open('../config/pageobject.json', mode='r') as f:
                ss = json.loads(f.read())
                print(ss)
            elem = ss['login']['elem']
            locatetype = elem[0]
            locatorExpression = elem[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj

        except Exception as e:
            raise e

    def nameObj(self):  # 单个元素的获取方法
        try:
            with open('../config/pageobject.json', mode='r') as f:
                ss = json.loads(f.read())
                print(ss)
            name = ss['login']['name']
            locatetype = name[0]
            locatorExpression = name[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e

    def passwdObj(self):  # 单个元素的获取方法
        try:
            with open('../config/pageobject.json', mode='r') as f:
                ss = json.loads(f.read())
                print(ss)
            passwd = ss['login']['passwd']
            locatetype = passwd[0]
            locatorExpression = passwd[1]
            self.ge = ge(self.driver, locatetype, locatorExpression)
            elemetObj = self.ge
            return elemetObj
        except Exception as e:
            raise e

if __name__ == '__main__':
    from selenium import webdriver
    dr = webdriver.Chrome()
    dr.get("http://118.24.211.165:8081")
    log = login(dr)
    log.elemObj()
    # log.nameObj()
    # log.passwdObj()