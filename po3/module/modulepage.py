import json
from selenium import webdriver
from util.wait import getElementWebDriverWait


class Element_page():
    def __init__(self, driver):
        self.driver = driver

    def kyObj(self):
        try:
            with open(r"C:\Users\xxx\PycharmProjects\untitled\po3\config\element.json", "r", encoding="utf-8") as  f:
                dicts = json.loads(f.read())

            lists = dicts['ky']
            locatuType = lists[0]
            locatorElement = lists[1]
            element = getElementWebDriverWait(self.driver, locatuType, locatorElement)
            return element
        except Exception as e:
            raise e
        
        
    def user_value(self):
        try:
            with open(r"C:\Users\xxx\PycharmProjects\untitled\po3\config\user.json", "r", encoding="utf-8") as  f:
                dicts = json.loads(f.read())

            user = dicts['user']
            return user
        except Exception as e:
            raise e
            
    def passwd_value(self):
        try:
            with open(r"C:\Users\xxx\PycharmProjects\untitled\po3\config\user.json", "r", encoding="utf-8") as  f:
                dicts = json.loads(f.read())

            passwd = dicts['passwd']
            return passwd
        except Exception as e:
            raise e
        
    def userObj(self):
        try:
            with open(r"C:\Users\xxx\PycharmProjects\untitled\po3\config\element.json", "r", encoding="utf-8") as  f:
                dicts = json.loads(f.read())

            lists = dicts['login']['user']
            locatuType = lists[0]
            locatorElement = lists[1]
            element = getElementWebDriverWait(self.driver, locatuType, locatorElement)
            return element
        except Exception as e:
            raise e
        
    def passwdObj(self):
        try:
            with open(r"C:\Users\xxx\PycharmProjects\untitled\po3\config\element.json", "r", encoding="utf-8") as  f:
                dicts = json.loads(f.read())

            lists = dicts['login']['passwd']
            locatuType = lists[0]
            locatorElement = lists[1]
            element = getElementWebDriverWait(self.driver, locatuType, locatorElement)
            return element
        except Exception as e:
            raise e
        
    def btnObj(self):
        try:
            with open(r"C:\Users\xxx\PycharmProjects\untitled\po3\config\element.json", "r", encoding="utf-8") as  f:
                dicts = json.loads(f.read())

            lists = dicts['login']['btn']
            locatuType = lists[0]
            locatorElement = lists[1]
            element = getElementWebDriverWait(self.driver, locatuType, locatorElement)
            return element
        except Exception as e:
            raise e
        
    def zuzhiObj(self):
        try:
            with open(r'C:\Users\xxx\PycharmProjects\untitled\po3\config\element.json','r',encoding='utf-8') as f:
                dicts=json.loads(f.read())
            lists=dicts['zuzhi']
            locatuType=lists[0]
            locatorElement=lists[1]
            element=getElementWebDriverWait(self.driver,locatuType,locatorElement)
            
            return element
        except Exception as e:
            raise  e

    def bumenObj(self):
        try:
            with open(r'C:\Users\xxx\PycharmProjects\untitled\po3\config\element.json', 'r', encoding='utf-8') as f:
                dicts = json.loads(f.read())
            lists = dicts['bumen']
            locatuType = lists[0]
            locatorElement = lists[1]
            element = getElementWebDriverWait(self.driver, locatuType, locatorElement)

            return element
        except Exception as e:
            raise e

    def iObj(self):
        try:
            with open(r'C:\Users\xxx\PycharmProjects\untitled\po3\config\element.json', 'r', encoding='utf-8') as f:
                dicts = json.loads(f.read())
            lists = dicts['i']
            locatuType = lists[0]
            locatorElement = lists[1]
            element = getElementWebDriverWait(self.driver, locatuType, locatorElement)

            return element
        except Exception as e:
            raise e

    def xiaoObj(self):
        try:
            with open(r'C:\Users\xxx\PycharmProjects\untitled\po3\config\element.json', 'r', encoding='utf-8') as f:
                dicts = json.loads(f.read())
            lists = dicts['xiao']
            locatuType = lists[0]
            locatorElement = lists[1]
            element = getElementWebDriverWait(self.driver, locatuType, locatorElement)

            return element
        except Exception as e:
            raise e

    def addObj(self):
        try:
            with open(r'C:\Users\xxx\PycharmProjects\untitled\po3\config\element.json', 'r', encoding='utf-8') as f:
                dicts = json.loads(f.read())
            lists = dicts['add_value']
            locatuType = lists[0]
            locatorElement = lists[1]
            element = getElementWebDriverWait(self.driver, locatuType, locatorElement)

            return element
        except Exception as e:
            raise e

    def bumen_value(self):
        try:
            with open(r'C:\Users\xxx\PycharmProjects\untitled\po3\config\bumen_values.json','r',encoding='UTF-8') as f:
                dicts=json.loads(f.read())
            bumen_value=dicts["bumen1"]

            return bumen_value
        except Exception as e:
            raise e

    def addbumenObj(self):
        try:
            with open(r'C:\Users\xxx\PycharmProjects\untitled\po3\config\element.json','r',encoding='UTF-8')  as f:
                dicts=json.loads(f.read())
            lists=dicts['add_bumen']

            locatuType=lists[0]
            locatorElement=lists[1]
            element=getElementWebDriverWait(self.driver,locatuType,locatorElement)
            return element
        except Exception as e:
            raise e



if __name__ == '__main__':
    driver = webdriver.Chrome()

