from page_object.page_obj import Add_User
from moudle.manipulation_login import Manipulation
from util.Parsing_json import Parsing_Json
from selenium import webdriver
import time
class Adding_User_Functions():
    def __init__(self,driver):
        self.page = Add_User(driver)
        self.parse = Parsing_Json()
        self.login = Manipulation(driver)

    def add_user_functions(self):
        self.login.login()
        self.page.parsing_zuzhi().click()
        self.page.add_user_btn().click()
        self.page.parsing_username_box().send_keys(self.parse.parsing_monolayer(r'../config/adduser_info.json',"username"))
        self.page.parsing_password_box().send_keys(self.parse.parsing_monolayer(r'../config/adduser_info.json',"password"))
        self.page.parsing_real_password_box().send_keys(self.parse.parsing_monolayer(r'../config/adduser_info.json',"real_password"))
        self.page.parsing_real_username_box().send_keys(self.parse.parsing_monolayer(r'../config/adduser_info.json',"real_username"))

if __name__ == '__main__':
    Adding_User_Functions(webdriver.Chrome()).add_user_functions()
