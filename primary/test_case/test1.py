import unittest,time
from moudle.manipulation_login import Manipulation
from moudle.add_user_ import Adding_User_Functions
from util.Parsing_json import Parsing_Json
from selenium import webdriver
class Test_1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.parse = Parsing_Json()
        self.add_user_obj = Adding_User_Functions(self.driver)
        self.driver.get(self.parse.parsing_monolayer(r'../config/url.json',"url"))
        self.man = Manipulation(self.driver)

    def tearDown(self):
        time.sleep(30)
        self.driver.quit()
    def test_add_user(self):
        self.man.login()