from util.parsejson import parsedingwei as pl
from util.util import getElementImplicitWait as ge
class Login():
    def __init__(self,driver):
        self.driver = driver

    def zentao(self):
        zentao = pl("login","zentao")
        strategy = zentao[0]
        locator = zentao[1]
        loginbtn = ge(self.driver,strategy,locator)
        return loginbtn

    def user(self):
        account = pl("login","account")
        id = account[0]
        content = account[1]
        user_c=ge(self.driver,id,content)
        return user_c

    def pwd(self):
        password = pl("login","password")
        name = password[0]
        content = password[1]
        pwd = ge(self.driver,name,content)
        return pwd

    def dengluanniu(self):
        enter_1 = pl("login","enter")
        id = enter_1[0]
        content = enter_1[1]
        enter = ge(self.driver,id,content)
        return enter
