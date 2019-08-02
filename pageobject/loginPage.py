#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/1 15:36
# @Author  : 郭轩甫
# @Site    : 
# @File    : loginpage.py
# @Software: PyCharm

import json
from selenium import webdriver
from util.wait import getElementImplicitWait as ge
class login:
    def __init__(self,driver):
        self.driver=driver


    def zenObj(self):
        try:
            with open('../config/pageobject.json', 'r', encoding='utf-8') as f:
                sw = json.loads(f.read())
            ss = sw["login"]["zentao"]
            locatetype = ss[0]
            locatorExpression = ss[1]
            print(1111)
            print(locatetype,locatorExpression)
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e

    def userRead(self):
        try:
            with open('../config/user.json','r',encoding='utf-8' ) as  f:
                sw=json.loads(f.read())
            user1=sw['user']
            print(user1)
            return user1
        except Exception as e:
            raise e

    def pwdRead(self):
        try:
            with open('../config/user.json','r',encoding='utf-8' ) as  f:
                sw=json.loads(f.read())
            pwd=sw['password']
            print(pwd)
            return pwd
        except Exception as e:
            raise e

    def nameObj(self):
        try:
            with open('../config/pageobject.json', 'r', encoding='utf-8') as f:
                sw = json.loads(f.read())
            ss = sw["login"]["name"]
            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e

    def passwordObj(self):
        try:
            with open('../config/pageobject.json', 'r', encoding='utf-8') as f:
                sw = json.loads(f.read())
            ss = sw["login"]["password"]
            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e

    def btnObj(self):
        try:
            with open('../config/pageobject.json', 'r', encoding='utf-8') as f:
                sw = json.loads(f.read())
            ss = sw["login"]["btn"]
            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj

        except Exception as e:
            raise e

    def zuzhiObj(self):
        try:
            with open('../config/pageobject.json', 'r', encoding='utf-8') as f:
                sw = json.loads(f.read())
            ss = sw["login"]["zuzhi"]
            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj

        except Exception as e:
            raise e

    def addObj(self):
        try:
            with open('../config/pageobject.json', 'r', encoding='utf-8') as f:
                sw = json.loads(f.read())
            ss = sw["login"]["add"]
            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj

        except Exception as e:
            raise e

if __name__=='__main__':
    driver=webdriver.Chrome()
    logins=login(driver)