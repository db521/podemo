from selenium import webdriver
from util.wait import getElementWait as ge
import json


class Zhou_log:

    def __init__(self,driver):
        self.driver = driver

    def read_Element(self):

        try:
            with open('D:\PO\zhoukao\config\element.json','r',encoding='utf-8') as f:
                butt = json.loads(f.read())
                butto = butt['cli']
                locatetype = butto["zen"][0]
                locateExpression = butto["zen"][1]
                element_obj = ge(self.driver,locatetype,locateExpression)

                return element_obj
        except Exception as e:
            raise e


    def read_Login_User(self):

        try:
            with open('D:\PO\zhoukao\config\element.json', 'r', encoding='utf-8') as f:
                butt = json.loads(f.read())
                butto = butt["user"]
                locatetype = butto["zhang"][0]
                locateExpression = butto["zhang"][1]
                element_obj = ge(self.driver, locatetype, locateExpression)

                return element_obj
        except Exception as e:
            raise e

    def read_Login_Password(self):

        try:
            with open('D:\PO\zhoukao\config\element.json', 'r', encoding='utf-8') as f:
                butt = json.loads(f.read())
                butto = butt["user"]
                locatetype = butto["password"][0]
                locateExpression = butto["password"][1]
                element_obj = ge(self.driver, locatetype, locateExpression)

                return element_obj
        except Exception as e:
            raise e

    def read_Login_Button(self):

        try:
            with open('D:\PO\zhoukao\config\element.json', 'r', encoding='utf-8') as f:
                butt = json.loads(f.read())
                butto = butt["button"]
                locatetype = butto[0]
                locateExpression = butto[1]
                element_obj = ge(self.driver, locatetype, locateExpression)

                return element_obj
        except Exception as e:
            raise e


if __name__ == '__main__':

    driver = webdriver.Chrome()
    Zhou_log(driver)
