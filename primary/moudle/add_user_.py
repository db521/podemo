from page_object.page_obj import Add_User
from util.Parsing_json import Parsing_Json
from moudle.manipulation_login import Manipulation
from selenium.webdriver.support.select import Select

class Adding_User_Functions():
    def __init__(self,driver):
        self.page = Add_User(driver)
        self.parse = Parsing_Json()
        self.login = Manipulation(driver)

    def add_user_functions(self):
        try:
            self.login.login()
            self.page.parsing_zuzhi().click()
            self.page.add_user_btn().click()

            self.page.parsing_username_box().send_keys(self.parse.parsing_monolayer(r'../config/adduser_info.json',"username"))
            self.page.parsing_password_box().send_keys(self.parse.parsing_monolayer(r'../config/adduser_info.json',"password"))

            self.page.parsing_real_password_box().send_keys(self.parse.parsing_monolayer(r'../config/adduser_info.json',"real_password"))
            self.page.parsing_real_username_box().send_keys(self.parse.parsing_monolayer(r'../config/adduser_info.json',"real_username"))

            Select(self.page.parsing_ranking()).select_by_index(2)

            #Select(self.page.parsing_group()).select_by_index(3)
            self.page.parsing_email().send_keys(self.parse.parsing_monolayer(r'../config/adduser_info.json',"email"))
            self.page.parsing_commiter().send_keys(self.parse.parsing_monolayer(r'../config/adduser_info.json',"commiter"))

            self.page.parsing_genderf().click()
            self.page.parsing_verifyPassword().send_keys(self.parse.parsing_monolayer(r'../config/adduser_info.json',"verifyPassword"))

            self.page.parsing_Preservation().click()
        except Exception as e:
            raise e


