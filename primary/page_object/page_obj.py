from util.util import Display_wait
from util.Parsing_json import Parsing_Json

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

    def parsing_group(self):
        group_obj = self.parse.parsing_strategy_locators(r'../config/login.json',"add_user_page","group")
        print(group_obj)
        return self.wait.get_element_display_wait(group_obj[0],group_obj[1])

    def parsing_email(self):
        email_obj = self.parse.parsing_strategy_locators(r'../config/login.json',"add_user_page","email")
        return self.wait.get_element_display_wait(email_obj[0],email_obj[1])

    def parsing_commiter(self):
        commiter_obj = self.parse.parsing_strategy_locators(r'../config/login.json',"add_user_page","commiter")
        return self.wait.get_element_display_wait(commiter_obj[0],commiter_obj[1])

    def parsing_genderf(self):
        genderf_obj = self.parse.parsing_strategy_locators(r'../config/login.json',"add_user_page","genderf")
        return self.wait.get_element_display_wait(genderf_obj[0],genderf_obj[1])

    def parsing_verifyPassword(self):
        verifyPassword_obj = self.parse.parsing_strategy_locators(r'../config/login.json',"add_user_page","system_pwd")
        return self.wait.get_element_display_wait(verifyPassword_obj[0],verifyPassword_obj[1])

    def parsing_Preservation(self):
        Preservation_obj = self.parse.parsing_strategy_locators(r'../config/login.json',"add_user_page","Preservation")
        return self.wait.get_element_display_wait(Preservation_obj[0],Preservation_obj[1])


