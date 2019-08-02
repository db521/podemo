import json
from until.wait import getElementImplicitWait as ge
from selenium import webdriver
class login:
    def __init__(self,driver):
        self.driver = driver
    def userRead(self):
        try:
            with open('../config/user.json','r',encoding='utf-8')as f:
                sw = json.loads(f.read())
            user1 = sw['user']
            print(user1)
            return user1
        except Exception as e:
            raise e
    def pwdRead(self):
        try:
            with open('../config/user.json','r',encoding='utf-8')as f:
                sw = json.loads(f.read())
            pwd = sw['passwd']
            print(pwd)
            return pwd
        except Exception as e:
            raise e
    def nameObj(self):
        try:
            with open('../config/pageobject.json','r',encoding='utf-8')as f:
                sw = json.loads(f.read())
            ss = sw["login"]["name"]
            locatetype = ss[0]
            locatorExpression = ss[1]
            elemetObj = ge(self.driver,locatetype,locatorExpression)
            return elemetObj
        except Exception as e:
            raise e