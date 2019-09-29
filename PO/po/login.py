# -*- coding: utf-8 -*-
from util.parsejson import parselocator as pl
from util.util import getElementImplicitWait as ge


class Login():
    def __init__(self, driver):
        self.driver = driver

    def zentao(self):
        zentao = pl("login", "zentao")
        strategy = zentao[0]
        locator = zentao[1]
        loginbtn = ge(self.driver, strategy, locator)
        return loginbtn

    def passwd(self):
        zentao = pl("login", "zentao")
        strategy = zentao[0]
        locator = zentao[1]
        loginbtn = ge(self.driver, strategy, locator)
        return loginbtn
