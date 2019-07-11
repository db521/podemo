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
            with open('../config/pageobject.json', 'r') as f:
                result = json.loads(f.read())
            elem = result["login"]["elem"]
            locatetype = elem[0]
            locatorExpression = elem[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e

    def nameObj(self):  # 单个元素的获取方法
        try:
            # ss = json.loads('./config/pageobject.json')["login"]["name"]

            with open('../config/pageobject.json', 'r') as f:
                result = json.loads(f.read())
            name = result["login"]["name"]
            locatetype = name[0]
            locatorExpression = name[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj

        except Exception as e:
            raise e

    def passwdObj(self):  # 单个元素的获取方法
        try:
            # ss = json.loads('./config/pageobject.json')["login"]["passwd"]
            with open('../config/pageobject.json', 'r') as f:
                result = json.loads(f.read())
            passwd = result["login"]["passwd"]
            locatetype = passwd[0]
            locatorExpression = passwd[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e

    def urlObj(self):
        try:
            with open('..\config\config.json', 'r') as a:
                wen = json.loads(a.read())
            url = wen['url']
            return url
        except Exception as e:
            raise e

    def userObj(self):
        try:
            with open('..\config\hao.json', 'r') as f:
                zuo = json.loads(f.read())
            user = zuo["login1"]["user"]
            return user
        except Exception as e:
            raise e

    def pwdObj(self):
        try:
            with open('..\config\hao.json', 'r') as f:
                zuo = json.loads(f.read())
                passwd = zuo["login1"]["passwd"]
            return passwd
        except Exception as e:
            raise e

    def subObj(self):
        try:
            with open('../config/pageobject.json','r') as f:
                result = json.loads(f.read())
            deng = result["login"]["submit"]
            locatetype = deng[0]
            locatorExpression = deng[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj

        except Exception as e:
            raise e

    def companyObj(self):
        try:
            with open('../config/pageobject.json','r') as f:
                result = json.loads(f.read())
            company = result["login"]["company"]
            locatetype = company[0]
            locatorExpression = company[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj
        except Exception as e:
            raise e

    def useraddObj(self):
        try:
            with open('../config/pageobject.json', 'r') as f:
                result = json.loads(f.read())
            useradd = result["login"]["useradd"]
            locatetype = useradd[0]
            locatorExpression = useradd[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj

        except Exception as e:
            raise e

    def add_chosenObj(self):
        try:
            with open('../config/useradd.json', 'r') as f:
                result = json.loads(f.read())
            chosen = result["add"]["chosen"]
            locatetype = chosen[0]
            locatorExpression = chosen[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj

        except Exception as e:
            raise e

    def add_deptObj(self):
        try:
            with open('../config/useradd.json', 'r') as f:
                result = json.loads(f.read())
            dept = result["add"]["dept"]
            locatetype = dept[0]
            locatorExpression = dept[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj

        except Exception as e:
            raise e

    def add_nameObj(self):
        try:
            with open('../config/useradd.json', 'r') as f:
                result = json.loads(f.read())
            name = result["add"]["name"]
            locatetype = name[0]
            locatorExpression = name[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj

        except Exception as e:
            raise e

    def add_pwd1Obj(self):
        try:
            with open('../config/useradd.json', 'r') as f:
                result = json.loads(f.read())
            pwd1 = result["add"]["pwd1"]
            locatetype = pwd1[0]
            locatorExpression = pwd1[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj

        except Exception as e:
            raise e

    def add_pwd2Obj(self):
        try:
            with open('../config/useradd.json', 'r') as f:
                result = json.loads(f.read())
            pwd2 = result["add"]["pwd2"]
            locatetype = pwd2[0]
            locatorExpression = pwd2[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj

        except Exception as e:
            raise e

    def add_realObj(self):
        try:
            with open('../config/useradd.json', 'r') as f:
                result = json.loads(f.read())
            real = result["add"]["real"]
            locatetype = real[0]
            locatorExpression = real[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj

        except Exception as e:
            raise e

    def add_roleObj(self):
        try:
            with open('../config/useradd.json', 'r') as f:
                result = json.loads(f.read())
            role = result["add"]["role"]
            locatetype = role[0]
            locatorExpression = role[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj

        except Exception as e:
            raise e

    def add_topObj(self):
        try:
            with open('../config/useradd.json', 'r') as f:
                result = json.loads(f.read())
            top = result["add"]["top"]
            locatetype = top[0]
            locatorExpression = top[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj

        except Exception as e:
            raise e

    def add_choObj(self):
        try:
            with open('../config/useradd.json', 'r') as f:
                result = json.loads(f.read())
            chosen1 = result["add"]["chosen1"]
            locatetype = chosen1[0]
            locatorExpression = chosen1[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj

        except Exception as e:
            raise e

    def add_groupObj(self):
        try:
            with open('../config/useradd.json', 'r') as f:
                result = json.loads(f.read())
            group = result["add"]["group"]
            locatetype = group[0]
            locatorExpression = group[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj

        except Exception as e:
            raise e

    def add_verifyObj(self):
        try:
            with open('../config/useradd.json', 'r') as f:
                result = json.loads(f.read())
            verify = result["add"]["verify"]
            locatetype = verify[0]
            locatorExpression = verify[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj

        except Exception as e:
            raise e

    def add_userObj(self):
        try:
            with open('..\config\hao.json', 'r') as f:
                zuo = json.loads(f.read())
            user = zuo["login1"]["user1"]
            return user
        except Exception as e:
            raise e

    def add_firpwdObj(self):
        try:
            with open('..\config\hao.json', 'r') as f:
                zuo = json.loads(f.read())
                passwd = zuo["login1"]["pwd1"]
            return passwd
        except Exception as e:
            raise e

    def add_secpwdObj(self):
        try:
            with open('..\config\hao.json', 'r') as f:
                zuo = json.loads(f.read())
                passwd = zuo["login1"]["pwd2"]
            return passwd
        except Exception as e:
            raise e

    def add_realnameObj(self):
        try:
            with open('..\config\hao.json', 'r') as f:
                zuo = json.loads(f.read())
                real = zuo["login1"]["real"]
            return real
        except Exception as e:
            raise e

    def syspwdObj(self):
        try:
            with open('..\config\hao.json', 'r') as f:
                zuo = json.loads(f.read())
                passwd = zuo["login1"]["passwd"]
            return passwd
        except Exception as e:
            raise e

    def saveObj(self):
        try:
            with open('../config/useradd.json', 'r') as f:
                result = json.loads(f.read())
            submit = result["add"]["submit"]
            locatetype = submit[0]
            locatorExpression = submit[1]
            elemetObj = ge(self.driver, locatetype, locatorExpression)
            return elemetObj

        except Exception as e:
            raise e


if __name__ == '__main__':
    from selenium import webdriver

    driver = webdriver.Chrome()
    log = login(driver)
    log.nameObj()
    log.passwdObj()
    log.urlObj()
    log.userObj()
    log.pwdObj()
    log.subObj()
    log.companyObj()
    log.useraddObj()
