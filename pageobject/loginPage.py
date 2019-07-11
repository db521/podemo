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
            with open(r'E:\郭亚光\pycham的\python文件\podemo\config\pageobject.json','r') as f:
                sname = json.loads(f.read())["login"]["name"]

            locatetype = sname[0]
            locatorExpression = sname[1]
            elemetObj1 = ge(self.driver, locatetype, locatorExpression)
            return elemetObj1
        except Exception as e:
            raise e

    def passwdObj(self):  # 单个元素的获取方法
        try:
            with open(r'E:\郭亚光\pycham的\python文件\podemo\config\pageobject.json','r') as fi:
                ss = json.loads(fi.read())["login"]["passwd"]
            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj2 = ge(self.driver, locatetype, locatorExpression)
            return elemetObj2
        except Exception as e:
            raise e

class login2:
    def __init__(self,driver):
        self.driver = driver
    def zuzhiObj(self):  #组织按钮
        try:
            with open(r'E:\郭亚光\pycham的\python文件\podemo\config\pageobject.json','r') as f3:
                zuzhi = json.loads(f3.read())['add']['zuzhi']

            locatetype = zuzhi[0]
            locatorExpression = zuzhi[1]
            elemetObj1 = ge(self.driver, locatetype, locatorExpression)
            return elemetObj1

        except Exception as e:
            raise e
    def tianjiaObj(self):  # 添加用户按钮
        try:
            with open(r'E:\郭亚光\pycham的\python文件\podemo\config\pageobject.json','r') as fi:
                ss = json.loads(fi.read())["add"]["tianjia"]
            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj2 = ge(self.driver, locatetype, locatorExpression)
            return elemetObj2
        except Exception as e:
            raise e
    def selectObj(self):  # select元素点击
        try:
            with open(r'E:\郭亚光\pycham的\python文件\podemo\config\pageobject.json','r') as fi:
                ss = json.loads(fi.read())["add"]["select"]
            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj2 = ge(self.driver, locatetype, locatorExpression)
            return elemetObj2
        except Exception as e:
            raise e
    def select2Obj(self):  # 选择班级
        try:
            with open(r'E:\郭亚光\pycham的\python文件\podemo\config\pageobject.json','r') as fi:
                ss = json.loads(fi.read())["add"]["select2"]
            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj2 = ge(self.driver, locatetype, locatorExpression)
            return elemetObj2
        except Exception as e:
            raise e