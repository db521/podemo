from util.Try_Page import *
from util.wait import GetWebDriverWait as ge

class Add:

    def __init__(self,driver):
        self.driver=driver

    def ZuzhiObj(self):
        return Try_Page(self.driver,"./config/pageobject.json","add","zuzhi",ge)

    def BumenObj(self):
        return Try_Page(self.driver, "./config/pageobject.json", "add", "bumen", ge)

    def AddObj(self):
        return Try_Page(self.driver, "./config/pageobject.json", "add", "add", ge)
