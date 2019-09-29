from util.parsejson import parselocator as pl
from util.util import getElementImplicitWait as ge

class Login():
    def __init__(self,driver):
        self.driver = driver

    def zentao(self):
        zentao = pl('login','zentao')
        strategy = zentao[0]
        locator = zentao[1]
        loginbtn = ge(self.driver,strategy,locator)
        return loginbtn

    def user(self):
        account = pl('login','account')
        stratgy = account[0]
        locator = account[1]
        loginuser = ge(self.driver,stratgy,locator)
        return loginuser

    def password(self):
        password = pl('login','password')
        stratgy = password[0]
        locator = password[1]
        loginpasswd = ge(self.driver,stratgy,locator)
        return loginpasswd
