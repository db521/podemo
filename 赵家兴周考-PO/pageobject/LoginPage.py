from util.Try_Page import *
from util.wait import GetWebDriverWait as ge

class Login:

    def __init__(self,driver):
        self.driver=driver

    def UserObj(self):
        return Try_Page(self.driver,"./config/pageobject.json","login","user",ge)

    def PasswdObj(self):
        return Try_Page(self.driver, "./config/pageobject.json", "login", "passwd", ge)

    def SubmitObj(self):
        return Try_Page(self.driver, "./config/pageobject.json", "login", "submit", ge)
