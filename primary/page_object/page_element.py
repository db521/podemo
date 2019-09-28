from util.Parsing_json import Parsing_Json
from util.util import Display_wait
from selenium import webdriver
class Page_obj():

    def __init__(self,driver):
        self.parse = Parsing_Json()
        self.driver = driver
        self.wait = Display_wait(self.driver)

    def zentao(self):
        url = self.parse.parsing_monolayer(r"../config/url.json","url")
        self.wait.visit_url(url)
        zentao = self.parse.parsing_strategy_locators(r'../config/login.json',"login","zentao")
        return self.wait.get_element_display_wait(zentao[0],zentao[1])

    def username_box(self):
        user_obj = self.parse.parsing_strategy_locators(r'../config/login.json',"login","username_box")
        print(user_obj)
        return self.wait.get_element_display_wait(user_obj[0],user_obj[1])

    def password_box(self):
        password_obj = self.parse.parsing_strategy_locators(r'../config/login.json', "login", "password_box")
        print(password_obj)
        return self.wait.get_element_display_wait(password_obj[0], password_obj[1])

    def login_btn_element(self):
        login_btn_obj = self.parse.parsing_strategy_locators(r'../config/login.json',"login","login_btn")
        return self.wait.get_element_display_wait(login_btn_obj[0],login_btn_obj[1])


if __name__ == '__main__':
    pass