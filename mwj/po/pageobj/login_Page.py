

from utils.wait import getWait as ge,gait
from utils.Try_Page import Try_Page

class ligin:
    def __init__(self,driver):
        self.driver = driver
        self.driver.maximize_window()


    def nameObj(self):
        return Try_Page(self.driver,'./config/page.json','login','name',ge)


    def passwdObj(self):
        return Try_Page(self.driver, './config/page.json', 'login', 'passwd', ge)

    def btnObj(self):
        return Try_Page(self.driver, './config/page.json', 'login', 'btn', ge)

    def useObj(self):
        return Try_Page(self.driver, './config/page.json', 'login', 'use', ge)

    def zhutiObj(self):
        Try_Page(self.driver,'./config/page.json','login','zhuti',gait)

    def besObj(self):
        return Try_Page(self.driver, './config/page.json', 'login', 'bes', ge)

    def zuzhiObj(self):
        return Try_Page(self.driver, './config/page.json', 'login', 'zuzhi', ge)

    def bumenObj(self):
        return Try_Page(self.driver, './config/page.json', 'login', 'bumen', ge)

    def addbmObj(self):
        return Try_Page(self.driver, './config/page.json', 'login', 'addbm', ge)

    def baocunObj(self):
        return Try_Page(self.driver, './config/page.json', 'login', 'baocun', ge)

    def delsObj(self):
        return Try_Page(self.driver, './config/page.json', 'login', 'dels', ge)
