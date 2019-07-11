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
                ss = json.loads(f.read())['login']['nname']
            # ss = json.loads('./config/pageobject.json')["login"]["name"]
            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e

    def passwdObj(self):  # 单个元素的获取方法
        try:
            with open('../config/pageobject.json',mode='r') as f:
                ss = json.loads(f.read())['login']['passwd']
            # ss = json.loads('./config/pageobject.json')["login"]["passwd"]
            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e

    def buttonObj(self):  # 单个元素的获取方法
        try:
            with open('../config/pageobject.json',mode='r') as f:
                ss = json.loads(f.read())['login']['but']
            # ss = json.loads('./config/pageobject.json')["login"]["passwd"]
            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e
    def aloginObj(self):  # 单个元素的获取方法
        try:
            with open('../config/pageobject.json',mode='r') as f:
                ss = json.loads(f.read())['login']['alogin']
            # ss = json.loads('./config/pageobject.json')["login"]["passwd"]
            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e

    def zuzhiObj(self):  # 单个元素的获取方法
        try:
            with open('../config/pageobject.json',mode='r') as f:
                ss = json.loads(f.read())['login']['zuzhi']
            # ss = json.loads('./config/pageobject.json')["login"]["passwd"]
            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e

    def adduserObj(self):  # 单个元素的获取方法
        try:
            with open('../config/pageobject.json',mode='r') as f:
                ss = json.loads(f.read())['login']['adduser']
            # ss = json.loads('./config/pageobject.json')["login"]["passwd"]
            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e

    def cliObj(self):  # 单个元素的获取方法
        try:
            with open('../config/pageobject.json',mode='r') as f:
                ss = json.loads(f.read())['login']['cli']
            # ss = json.loads('./config/pageobject.json')["login"]["passwd"]
            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e

    def bumenObj(self):  # 单个元素的获取方法
        try:
            with open('../config/pageobject.json',mode='r') as f:
                ss = json.loads(f.read())['login']['bumen']
            # ss = json.loads('./config/pageobject.json')["login"]["passwd"]
            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e

    def namesObj(self):  # 单个元素的获取方法
        try:
            with open('../config/pageobject.json',mode='r') as f:
                ss = json.loads(f.read())['login']['names']
            # ss = json.loads('./config/pageobject.json')["login"]["passwd"]
            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e

    def passwds1Obj(self):  # 单个元素的获取方法
        try:
            with open('../config/pageobject.json',mode='r') as f:
                ss = json.loads(f.read())['login']['passwds1']
            # ss = json.loads('./config/pageobject.json')["login"]["passwd"]
            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e

    def passwds2Obj(self):  # 单个元素的获取方法
        try:
            with open('../config/pageobject.json',mode='r') as f:
                ss = json.loads(f.read())['login']['passwds2']
            # ss = json.loads('./config/pageobject.json')["login"]["passwd"]
            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e

    def znameObj(self):  # 单个元素的获取方法
        try:
            with open('../config/pageobject.json',mode='r') as f:
                ss = json.loads(f.read())['login']['zname']
            # ss = json.loads('./config/pageobject.json')["login"]["passwd"]
            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e

    def testObj(self):  # 单个元素的获取方法
        try:
            with open('../config/pageobject.json',mode='r') as f:
                ss = json.loads(f.read())['login']['test']
            # ss = json.loads('./config/pageobject.json')["login"]["passwd"]
            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e


    def emailObj(self):  # 单个元素的获取方法
        try:
            with open('../config/pageobject.json',mode='r') as f:
                ss = json.loads(f.read())['login']['email']
            # ss = json.loads('./config/pageobject.json')["login"]["passwd"]
            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e

    def cnameObj(self):  # 单个元素的获取方法
        try:
            with open('../config/pageobject.json',mode='r') as f:
                ss = json.loads(f.read())['login']['cname']
            # ss = json.loads('./config/pageobject.json')["login"]["passwd"]
            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e

    def registerObj(self):  # 单个元素的获取方法
        try:
            with open('../config/pageobject.json',mode='r') as f:
                ss = json.loads(f.read())['login']['register']
            # ss = json.loads('./config/pageobject.json')["login"]["passwd"]
            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e
