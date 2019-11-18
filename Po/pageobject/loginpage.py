import json

from unittest.wait import getElement as ge


# 登陆模块
class login:

    def __init__(self, driver):
        self.driver = driver

    # 定位用户名输入框
    def nameObj(self):

        try:
            with open("../config/pageobject.json", 'r', encoding="utf-8") as f:
                dictname = json.loads(f.read())
            na = dictname["login"]["name"]
            locatetype = na[0]
            locatorExpression = na[1]
            elementObj = ge(self.driver, locatetype, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    # 定位密码输入框
    def passwdObj(self):
        try:
            with open("../config/pageobject.json", 'r', encoding="utf-8") as f:
                dictname = json.loads(f.read())
            na = dictname["login"]["passwd"]
            locatetype = na[0]
            locatorExpression = na[1]
            elementObj = ge(self.driver, locatetype, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    # 定位登陆按钮
    def buttonObj(self):
        try:
            with open("../config/pageobject.json", 'r', encoding="utf-8") as f:
                dictname = json.loads(f.read())
            na = dictname["login"]["button"]
            locatetype = na[0]
            locatorExpression = na[1]
            elementObj = ge(self.driver, locatetype, locatorExpression)
            return elementObj
        except Exception as e:
            raise e


if __name__ == '__main__':
    from selenium import webdriver

    driver = webdriver.Chrome()
    logins = login(driver)
    logins.nameObj()