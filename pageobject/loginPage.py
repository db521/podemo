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
            with open(r'C:\Users\Administrator\Desktop\pod\podemo\config\pageobject.json',mode='r') as f:
                ss=json.loads(f.read())['login']['user']
                locatetype = ss[0]
                locatorExpression = ss[1]
                elemetObj = ge(self.driver, locatetype, locatorExpression)
                return elemetObj
        except Exception as e:
            raise e

    def passwdObj(self):  # 单个元素的获取方法
        try:
            with open(r'C:\Users\Administrator\Desktop\pod\podemo\config\pageobject.json',mode='r')as f:
                ss = json.loads(f.read())['login']['passwd']
                locatetype = ss[0]
                locatorExpression = ss[1]
                elemetObj = ge(self.driver, locatetype, locatorExpression)
                return elemetObj
        except Exception as e:
            raise e

