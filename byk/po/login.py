# -*- coding: utf-8 -*-
from util.parsejson import parselocator as pl
from util.util import getElementImplicitwait as ge
class Login():
    def __init__(self,driver):
        self.driver=driver
    def zentao(self):
        zentao=pl("login", "zentao")
        startegy=zentao[0]
        locator=zentao[1]
        loginbtn=ge(self.driver,startegy,locator)
        return loginbtn
    def user(self):
        zentao=pl("login", "zentao")
        startegy=zentao[0]
        locator=zentao[1]
        loginbtn=ge(self.driver,startegy,locator)
        return loginbtn
    def passwd(self):
        zentao=pl("login", "zentao")
        startegy=zentao[0]
        locator=zentao[1]
        loginbtn=ge(self.driver,startegy,locator)
        return loginbtn