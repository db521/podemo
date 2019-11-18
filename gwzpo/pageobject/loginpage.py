from untils.get_page import *
from untils.wait import getWebDriver as ge

class Login:
    def __init__(self,driver):
        self.driver = driver
        self.driver.maximize_window()

    def UserObj(self):
        return get_page(self.driver,"../config/login.json","login","user",ge)

    def Passwordobj(self):
        return get_page(self.driver,"../config/login.json","login","passwd",ge)

    def Loginobj(self):
        return get_page(self.driver,"../config/login.json","login","login",ge)