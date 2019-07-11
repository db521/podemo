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
            with open("../config/pageobject.json",mode="r") as f:
                ss = json.loads(f.read())

            name = ss['login']["user"]
            locatetype = name[0]
            locatorExpression = name[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e

    def passwdObj(self):  # 单个元素的获取方法
        try:
            with open("../config/pageobject.json",mode="r")as f:
                aa = json.loads(f.read())
                user = aa["login"]["passwd"]
                # passwd = aa["login"]["passwd"]
            locatetype =user[0]
            locatorExpression = user[1]

            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e
    def loginObj(self):  # 单个元素的获取方法
        try:
            with open("../config/pageobject.json",mode="r")as f:
                aa = json.loads(f.read())
                user = aa["login"]["zandao"]
                # passwd = aa["login"]["passwd"]
            locatetype =user[0]
            locatorExpression = user[1]

            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e
    def submitObj(self):  # 单个元素的获取方法
        try:
            with open("../config/pageobject.json",mode="r") as f:
                ss = json.loads(f.read())

            name = ss['login']["submit"]
            locatetype = name[0]
            locatorExpression = name[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e
    def zuzhiObj(self):  # 单个元素的获取方法
        try:
            with open("../config/pageobject.json",mode="r") as f:
                ss = json.loads(f.read())

            name = ss['login']["zuzhi"]
            locatetype = name[0]
            locatorExpression = name[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e
    def addnameObj(self):  # 单个元素的获取方法
        try:
            with open("../config/pageobject.json",mode="r") as f:
                ss = json.loads(f.read())

            name = ss['login']["addname"]
            locatetype = name[0]
            locatorExpression = name[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e

    def listsObj(self):  # 单个元素的获取方法
        try:
            with open("../config/pageobject.json",mode="r") as f:
                ss = json.loads(f.read())

            name = ss['login']["lists"]
            locatetype = name[0]
            locatorExpression = name[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e

    def listlObj(self):  # 单个元素的获取方法
        try:
            with open("../config/pageobject.json",mode="r") as f:
                ss = json.loads(f.read())

            name = ss['login']["listl"]
            locatetype = name[0]
            locatorExpression = name[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e
    def usernameObj(self):  # 单个元素的获取方法
        try:
            with open("../config/pageobject.json",mode="r") as f:
                ss = json.loads(f.read())

            name = ss['login']["username"]
            locatetype = name[0]
            locatorExpression = name[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e

    def passwd1Obj(self):  # 单个元素的获取方法
        try:
            with open("../config/pageobject.json",mode="r") as f:
                ss = json.loads(f.read())

            name = ss['login']["passwds"]
            locatetype = name[0]
            locatorExpression = name[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e

    def passwd2Obj(self):  # 单个元素的获取方法
        try:
            with open("../config/pageobject.json",mode="r") as f:
                ss = json.loads(f.read())

            name = ss['login']["passwdx"]
            locatetype = name[0]
            locatorExpression = name[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e :
            raise e

    def realnameObj(self):  # 单个元素的获取方法
        try:
            with open("../config/pageobject.json",mode="r") as f:
                ss = json.loads(f.read())

            name = ss['login']["realname"]
            locatetype = name[0]
            locatorExpression = name[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e

    def positionObj(self):  # 单个元素的获取方法
        try:
            with open("../config/pageobject.json", mode="r") as f:
                ss = json.loads(f.read())

            name = ss['login']["position"]
            locatetype = name[0]
            locatorExpression = name[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e

    def emailObj(self):  # 单个元素的获取方法
        try:
            with open("../config/pageobject.json", mode="r") as f:
                ss = json.loads(f.read())

            name = ss['login']["email"]
            locatetype = name[0]
            locatorExpression = name[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e

    def verifypasswordObj(self):  # 单个元素的获取方法
        try:
            with open("../config/pageobject.json", mode="r") as f:
                ss = json.loads(f.read())

            name = ss['login']["verifypassword"]
            locatetype = name[0]
            locatorExpression = name[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e

    def dianjiObj(self):  # 单个元素的获取方法
        try:
            with open("../config/pageobject.json", mode="r") as f:
                ss = json.loads(f.read())

            name = ss['login']["dianji"]
            locatetype = name[0]
            locatorExpression = name[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e