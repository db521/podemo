from utils.wait import get_elementObj
from utils.page import ele_single
import json

class Login_CD:
    def __init__(self,driver):
        self.driver = driver
        self.driver.maximize_window()

    def userObj(self):
        return get_elementObj(self.driver,ele_single("login","user")[0],ele_single("login","user")[1])

    def passwdObj(self):
        return get_elementObj(self.driver, ele_single("login", "passwd")[0], ele_single("login", "passwd")[1])

    def login_btn(self):
        return get_elementObj(self.driver, ele_single("login", "login_btn")[0], ele_single("login", "login_btn")[1])

if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    lg = Login_CD(driver)
    print(lg.userObj())