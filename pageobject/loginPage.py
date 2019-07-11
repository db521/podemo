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
            with open(r'C:\Users\10953\Desktop\daiam\podemo\config\pageobject.json',mode='r')as f:
                ss = json.loads(f.read())['login']['name']

            # ss = json.loads('./config/pageobject.json')["login"]["name"]
            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e

    def passwdObj(self):  # 单个元素的获取方法
        try:
            with open(r'C:\Users\10953\Desktop\daiam\podemo\config\pageobject.json',mode='r')as f:
                ss = json.loads(f.read())['login']['passwd']
            # ss = json.loads('./config/pageobject.json')["login"]["passwd"]
            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e

    def bntObj(self):
        try:
            with open(r'C:\Users\10953\Desktop\daiam\podemo\config\pageobject.json', mode='r')as f:
                ss = json.loads(f.read())['login']['bnt']

            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj

        except Exception as e:
            raise e

    def zzObj(self):
        try:
            with open(r'C:\Users\10953\Desktop\daiam\podemo\config\pageobject.json', mode='r')as f:
                ss = json.loads(f.read())['login']['zz']

            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj

        except Exception as e:
            raise e

    def yhObj(self):
        try:
            with open(r'C:\Users\10953\Desktop\daiam\podemo\config\pageobject.json', mode='r')as f:
                ss = json.loads(f.read())['login']['yh']

            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj

        except Exception as e:
            raise e

    def seObj(self):
        try:
            with open(r'C:\Users\10953\Desktop\daiam\podemo\config\pageobject.json', mode='r')as f:
                ss = json.loads(f.read())['login']['se']

            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj

        except Exception as e:
            raise e
    def cObj(self):
        try:
            with open(r'C:\Users\10953\Desktop\daiam\podemo\config\pageobject.json', mode='r')as f:
                ss = json.loads(f.read())['login']['c']

            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj

        except Exception as e:
            raise e

    def cnameObj(self):
        try:
            with open(r'C:\Users\10953\Desktop\daiam\podemo\config\pageobject.json', mode='r')as f:
                ss = json.loads(f.read())['login']['cname']

            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj

        except Exception as e:
            raise e

    def pwdObj(self):
        try:
            with open(r'C:\Users\10953\Desktop\daiam\podemo\config\pageobject.json', mode='r')as f:
                ss = json.loads(f.read())['login']['pwd']

            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj

        except Exception as e:
            raise e

    def cpwdObj(self):
        try:
            with open(r'C:\Users\10953\Desktop\daiam\podemo\config\pageobject.json', mode='r')as f:
                ss = json.loads(f.read())['login']['cpwd']

            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj

        except Exception as e:
            raise e

    def znamedObj(self):
        try:
            with open(r'C:\Users\10953\Desktop\daiam\podemo\config\pageobject.json', mode='r')as f:
                ss = json.loads(f.read())['login']['zname']

            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj

        except Exception as e:
            raise e

    def xpwddObj(self):
        try:
            with open(r'C:\Users\10953\Desktop\daiam\podemo\config\pageobject.json', mode='r')as f:
                ss = json.loads(f.read())['login']['xpwd']

            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj

        except Exception as e:
            raise e