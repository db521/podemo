from util.Parsing_json import Parsing_Json
from util.util import Display_wait
class Add_User():
    def __init__(self,driver):
        self.parse = Parsing_Json()
        self.wait = Display_wait(driver)

    def parsing_zuzhi(self):
        zuzhi_obj = self.parse.parsing_strategy_locators(r'../config/login.json',"add_user_page","zuzhi")
        return self.wait.get_element_display_wait(zuzhi_obj[0],zuzhi_obj[1])

    def add_user_btn(self):
        add_user_obj = self.parse.parsing_strategy_locators(r'../config/login.json',"add_user_page","add_user_btn")
        return self.wait.get_element_display_wait(add_user_obj[0],add_user_obj[1])

    def parsing_username_box(self):
        username_obj = self.parse.parsing_strategy_locators(r'../config/login.json',"add_user_page","username")
        return self.wait.get_element_display_wait(username_obj[0],username_obj[1])

    def parsing_password_box(self):
        password_obj = self.parse.parsing_strategy_locators(r'../config/login.json',"add_user_page","password")
        return self.wait.get_element_display_wait(password_obj[0],password_obj[1])

    def parsing_real_password_box(self):
        real_password_obj = self.parse.parsing_strategy_locators(r'../config/login.json',"add_user_page","real_password")
        return self.wait.get_element_display_wait(real_password_obj[0],real_password_obj[1])

    def parsing_real_username_box(self):
        real_username_obj = self.parse.parsing_strategy_locators(r'../config/login.json',"add_user_page","real_username")
        return self.wait.get_element_display_wait(real_username_obj[0],real_username_obj[1])

    def parsing_ranking(self):
        ranking_obj = self.parse.parsing_strategy_locators(r'../config/login.json',"add_user_page","ranking")
        return self.wait.get_element_display_wait(ranking_obj[0],ranking_obj[1])
