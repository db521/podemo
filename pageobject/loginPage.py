#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/5 8:44
# @Author  : 郭轩甫
# @Site    : 
# @File    : loginpage.py
# @Software: PyCharm


import json
from selenium import webdriver
from util.wait import ElementWait as ge

class login:
    def __init__(self,driver):
        self.driver=driver
    def zenObg(self):
        try:
            with open('../config/pageobject.json','r',encoding='utf-8')as f:
                sw=json.loads(f.read())
            ss=sw['login']['zentao']
            loginType=ss[0]
            loginElement=ss[1]
            elemetObj=ge(self.driver,loginType,loginElement)
            return elemetObj
        except Exception as e:
            raise e


    def userRead(self):
        try:
            with open('../config/user.json','r',encoding='utf-8')as f:
                sw=json.loads(f.read())
            user=sw['user']
            print(user)
            return user
        except Exception as e:
            raise e

    def passwordRead(self):
        try:
            with open('../config/user.json','r',encoding='utf-8')as f:
                sw=json.loads(f.read())
            password=sw['password']
            return password
        except Exception as e:
            raise e

    def nameObg(self):
        try:
            with open('../config/pageobject.json','r',encoding='utf-8')as f:
                sw=json.loads(f.read())
            ss=sw['login']['name']
            loginType=ss[0]
            loginElement=ss[1]
            elemetObj=ge(self.driver,loginType,loginElement)
            return elemetObj
        except Exception as e:
            raise e

    def passwordObg(self):
        try:
            with open('../config/pageobject.json','r',encoding='utf-8')as f:
                sw=json.loads(f.read())
            ss=sw['login']['password']
            loginType=ss[0]
            loginElement=ss[1]
            elemetObj=ge(self.driver,loginType,loginElement)
            return elemetObj
        except Exception as e:
            raise e

    def btnObg(self):
        try:
            with open('../config/pageobject.json','r',encoding='utf-8')as f:
                sw=json.loads(f.read())
            ss=sw['login']['btn']
            loginType=ss[0]
            loginElement=ss[1]
            elemetObj=ge(self.driver,loginType,loginElement)
            return elemetObj
        except Exception as e:
            raise e

    def zuzhiObg(self):
        try:
            with open('../config/pageobject.json','r',encoding='utf-8')as f:
                sw=json.loads(f.read())
            ss=sw['login']['zuzhi']
            loginType=ss[0]
            loginElement=ss[1]
            elemetObj=ge(self.driver,loginType,loginElement)
            return elemetObj
        except Exception as e:
            raise e

    def addObg(self):
        try:
            with open('../config/pageobject.json','r',encoding='utf-8')as f:
                sw=json.loads(f.read())
            ss=sw['login']['add']
            loginType=ss[0]
            loginElement=ss[1]
            elemetObj=ge(self.driver,loginType,loginElement)
            return elemetObj
        except Exception as e:
            raise e

if __name__=='__main__':
    driver=webdriver.Chrome()
    logins=login(driver)