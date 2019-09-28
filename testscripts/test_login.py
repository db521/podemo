from selenium import webdriver
from modules.login_mod import LoginMod
from utils.read_json import read_url as ru
import unittest
class Login_class(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_log(self):
        self.driver.get(ru('login'))
        LoginMod(self.driver)

    def tearDown(self):
        self.driver.close()