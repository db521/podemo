import json
from selenium import webdriver
from util.util import getElementWebDriverWait as ge

class Element_page():
    def __init__(self,driver):
        self.driver =driver

    def kyObj(self):
        try:
            with open(r'C:\Users\Lenovo\Desktop\zendao\config\element.json','r',encoding='utf-8') as f:
                content = json.loads(f.read())

            lists = content['ky']
            locatuType = lists[0]
            locatorElement = lists[1]
            element = ge(self.driver,locatuType,locatorElement)
            return element
        except  Exception as e:
            raise e

    def name_value(self):
        try:
            with open(r'C:\Users\Lenovo\Desktop\zendao\config\user.json','r',encoding='utf-8') as f:
                dicts = json.loads(f.read())
            user=dicts['name']
            return user
        except Exception as e:
            raise e


    def nameObj(self):
        try:
            with open(r'C:\Users\Lenovo\Desktop\zendao\config\element.json','r',encoding='utf-8') as f:
                content1 = json.loads(f.read())

            users =content1['login']['user']
            locatuType = users[0]
            locatorElement = users[1]
            element = ge(self.driver,locatuType,locatorElement)
            return element
        except Exception as e:
            raise e


    def pwd_value(self):
        try:
            with open(r'C:\Users\Lenovo\Desktop\zendao\config\user.json','r',encoding='utf-8') as f:
                sw = json.loads(f.read())
            pwd = sw['passwd']
            return pwd
        except Exception as e:
            raise e


    def pwdObj(self):
        try:
            with open(r'C:\Users\Lenovo\Desktop\zendao\config\element.json','r',encoding='utf-8') as f:
                sw = json.loads(f.read())

            passwd = sw['login']['passwd']
            locatuType = passwd[0]
            locatorElement = passwd[1]
            element = ge(self.driver,locatuType,locatorElement)
            return element
        except Exception as e:
            raise e

    def butObj(self):
        try:
            with open(r'C:\Users\Lenovo\Desktop\zendao\config\element.json','r',encoding='utf-') as f:
                sw = json.loads(f.read())
            ss = sw['login']['btn']
            locatuType = ss[0]
            locatorElement = ss[1]
            element = ge(self.driver,locatuType,locatorElement)
            return element
        except Exception as e:
            raise e

    def zuObj(self):
        try:
            with open(r'C:\Users\Lenovo\Desktop\zendao\config\element.json','r',encoding='utf-8') as f:
                sw = json.loads(f.read())
            ss = sw['caozuo']['richeng']
            locatuType = ss[0]
            locatorElement = ss[1]
            element = ge(self.driver,locatuType,locatorElement)
            return element
        except Exception as e:
            raise e





