#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/30 17:01 
# @File : loginPage.py
import json
from util.wait import getElementImplicitWait as ge



class login:
    def __init__(self, driver):

        self.driver = driver

    def dian(self):
        self.elem = self.driver.find_element_by_id('zentao')
        self.elem.click()

    def nameObj(self):  # 单个元素的获取方法

        try:
            with open('../config/pageobject.json', 'r+', encoding='utf-8') as f:
                aa = json.loads(f.read())
                ss = aa['login']['name']
            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            print(elemetObj)
            return elemetObj
        except Exception as e:
            raise e

    def passwdObj(self):  # 单个元素的获取方法
        try:
            with open('../config/pageobject.json', 'r+', encoding='utf-8') as f:
                aa = json.loads(f.read())
                ss = aa['login']['passwd']
            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            print(elemetObj)
            return elemetObj
        except Exception as e:
            raise e
