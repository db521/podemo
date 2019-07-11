#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/30 17:01 
# @File : loginPage.py
import json
from util.wait import getElementImplicitWait as ge

with open('..\config\pageobject.json', 'r')as f:
    result = json.loads(f.read())
class login:
    def __init__(self, driver):
        self.driver = driver
    def ztObj(self):  # 单个元素的获取方法
        try:

            ss=result['login']['zt']
            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e
    def nameObj(self):  # 单个元素的获取方法
        try:
            ss=result['login']['name']
            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e

    def passwdObj(self):  # 单个元素的获取方法
        try:
            ss=result['login']['passwd']
            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e
    def zuzhi(self):  # 单个元素的获取方法
        try:
            ss=result['login']['zuzhi']
            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e
    def adduser(self):  # 单个元素的获取方法
        try:
            ss=result['login']['adduser']
            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e
    def el_sel(self):  # 单个元素的获取方法
        try:
            ss=result['login']['el_sel']
            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e
    def sel(self):  # 单个元素的获取方法
        try:
            ss=result['login']['sel']
            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e
    def uname(self):  # 单个元素的获取方法
        try:
            ss=result['login']['uname']
            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e
    def password1(self):  # 单个元素的获取方法
        try:
            ss=result['login']['password1']
            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e
    def password2(self):  # 单个元素的获取方法
        try:
            ss=result['login']['password2']
            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e
    def realname(self):  # 单个元素的获取方法
        try:
            ss=result['login']['realname']
            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e
    def join(self):  # 单个元素的获取方法
        try:
            ss=result['login']['join']
            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e
    def data(self):  # 单个元素的获取方法
        try:
            ss=result['login']['data']
            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e
    def role(self):  # 单个元素的获取方法
        try:
            ss=result['login']['role']
            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e
    def top(self):  # 单个元素的获取方法
        try:
            ss=result['login']['top']
            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e
    def email(self):  # 单个元素的获取方法
        try:
            ss=result['login']['email']
            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e
    def verifyPassword(self):  # 单个元素的获取方法
        try:
            ss=result['login']['verifyPassword']
            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e
    def submit(self):  # 单个元素的获取方法
        try:
            ss=result['login']['submit']
            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e