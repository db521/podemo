from util.wait import getWebDriverWait as ge
import json
class login():
    def __init__(self,driver):
        self.driver=driver
        self.driver.maximize_window()
    def userObj(self):
        try:
            with open("../config/pageobjects.json", "r",)as f:
                ss = json.loads(f.read())
            sw = ss["login"]["user"]
            locatetype =sw[0]
            locatevalue = sw[1]
            elementObj = ge(self.driver, locatetype, locatevalue)
            return elementObj
        except Exception as e:
            raise e

    def passwdObj(self):
        try:
            with open("../config/pageobjects.json", "r",)as f:
                ss = json.loads(f.read())
            sw = ss["login"]["passwd"]
            locatetype =sw[0]
            locatevalue = sw[1]
            elementObj = ge(self.driver,locatetype, locatevalue)
            return elementObj
        except Exception as e:
            raise e

    def btnObj(self):
        try:
            with open("../config/pageobjects.json", "r",)as f:
                ss = json.loads(f.read())
            sw = ss["login"]["btn"]
            locatetype =sw[0]
            locatevalue = sw[1]
            elementObj = ge(self.driver, locatetype, locatevalue)
            return elementObj
        except Exception as e:
            raise e