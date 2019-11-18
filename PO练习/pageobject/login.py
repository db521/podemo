import json
from util.wait import getWebDriverWait as ge

class Login:
    def __init__(self,driver):
        self.driver=driver
        self.driver.maximize_window()

    def UserObj(self):
        try:
            with open("../config/pageobject.json","r+",encoding="utf-8")as f:
                objs = json.loads(f.read())
            obj = objs['login']['user']
            locatype=obj[0]
            locavalue=obj[1]
            elementObj = ge(self.driver,locatype,locavalue)
            return elementObj

        except Exception as e:
            raise e


    def PasswdObj(self):
        try:
            with open("../config/pageobject.json","r+",encoding="utf-8")as f:
                objs = json.loads(f.read())
            obj = objs['login']['passwd']
            locatype=obj[0]
            locavalue=obj[1]
            elementObj = ge(self.driver,locatype,locavalue)
            return elementObj

        except Exception as e:
            raise e

    def LoginObj(self):
        try:
            with open("../config/pageobject.json","r+",encoding="utf-8")as f:
                objs = json.loads(f.read())
            obj = objs['login']['login']
            locatype=obj[0]
            locavalue=obj[1]
            elementObj = ge(self.driver,locatype,locavalue)
            return elementObj

        except Exception as e:
            raise e

