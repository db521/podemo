from page_object.page_element import Page_obj
from util.Parsing_json import Parsing_Json

class Manipulation():
    def __init__(self,driver):
        self.driver = driver
        self.parse = Parsing_Json()
        self.page = Page_obj(self.driver)

    def open_url(self):
        self.page.zentao().click()

    def login(self):
        try:
            self.open_url()
            self.page.username_box().send_keys(self.parse.parsing_monolayer(r'../config/user_info.json',"username"))
            self.page.password_box().send_keys(self.parse.parsing_monolayer(r'../config/user_info.json', "password"))
            self.page.login_btn_element().click()

        except Exception as e:
            raise e
