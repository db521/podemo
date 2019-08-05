from selenium import webdriver
import json
from util.wait import getElementImplicitWait

class login:
    def __init__(self,driver):
        self.driver = driver

    def btnobj(self):
        try:
            with open(r'D:\pachong2\podemo_1\config\pageobject.json','r',encoding='utf-8' ) as  f:
                dicts=json.loads(f.read())
            lists=dicts['login']['btn']
            btntype = lists[0]
            btnxp = lists[1]
            element = getElementImplicitWait(self.driver,btntype,btnxp)

            return element
        except Exception as e:
            raise e

    def use_value(self):
        try:
            with open(r'D:\pachong2\podemo_1\config\userlogin.json', 'r+',encoding='utf-8') as f:
                dicts = json.loads(f.read())
            user1 = dicts['name']
            return user1
        except Exception as e:
            raise e

    def passwd_value(self):
        try:
            with open(r'D:\pachong2\podemo_1\config\userlogin.json', 'r+',encoding='utf-8') as f:
                dicts = json.loads(f.read())
            password = dicts['password']
            return password
        except Exception as e:
            raise e

    def useobj(self):
        try:
            with open(r'D:\pachong2\podemo_1\config\pageobject.json','r',encoding='utf-8' ) as  f:
                dicts=json.loads(f.read())
            lists=dicts['login']['username']
            btntype = lists[0]
            btnxp = lists[1]
            element = getElementImplicitWait(self.driver,btntype,btnxp)
            return element
        except Exception as e:
            raise e

    def passwdobj(self):
        try:
            with open(r'D:\pachong2\podemo_1\config\pageobject.json','r',encoding='utf-8' ) as  f:
                dicts=json.loads(f.read())
            lists=dicts['login']['passwd']
            btntype = lists[0]
            btnxp = lists[1]
            element = getElementImplicitWait(self.driver,btntype,btnxp)
            return element
        except Exception as e:
            raise e

    def loginobj(self):
        try:
            with open(r'D:\pachong2\podemo_1\config\pageobject.json','r',encoding='utf-8' ) as  f:
                dicts=json.loads(f.read())
            lists=dicts['login']['logins']
            btntype = lists[0]
            btnxp = lists[1]
            element = getElementImplicitWait(self.driver,btntype,btnxp)
            return element
        except Exception as e:
            raise e

if __name__ == "__main__":
    driver = webdriver.Chrome()
