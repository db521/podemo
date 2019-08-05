import json
from utils.wait import Webdriverait as ge
from selenium import webdriver


class access:
    def __init__(self, driver):
        self.driver = driver

    def userREd(self):
        try:
            with open("../config/users.json", "r", encoding="utf-8")as f:
                su = json.loads(f.read())
            we = su["user"]
            print(we)
            return we
        except Exception as e:
            raise e

    def pwdREd(self):
        try:
            with open("../config/users.json", "r", encoding="utf-8")as f:
                su = json.loads(f.read())
            we = su["pwd"]
            print(we)
            return we
        except Exception as e:
            raise e

    def userObj(self):
        try:
            with open("../config/pageobjects.json", "r", encoding="utf-8")as f:
                su = json.loads(f.read())
            we = su["access"]["name"]
            wtype = we[0]
            lption = we[1]
            elementObj = ge(self.driver, wtype, lption)
            return elementObj
        except Exception as e:
            raise e

    def pwdObj(self):
        try:
            with open("../config/pageobjects.json", "r", encoding="utf-8")as f:
                su = json.loads(f.read())
            we = su["access"]["passwd"]
            wtype = we[0]
            lption = we[1]
            elementObj = ge(self.driver, wtype, lption)
            return elementObj
        except Exception as e:
            raise e

    def btnObj(self):
        try:
            with open("../config/pageobjects.json", "r", encoding="utf-8")as f:
                su = json.loads(f.read())
            we = su["access"]["btn"]
            wtype = we[0]
            lption = we[1]
            elementObj = ge(self.driver, wtype, lption)
            return elementObj
        except Exception as e:
            raise e


if __name__ == '__main__':
    driver = webdriver.Chrome()
    assecct = access(driver)
    assecct.userObj()
