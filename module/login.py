from po.login import Login
from util.parsejson import UserInfo
from selenium.webdriver.common.keys import Keys
import time

username = UserInfo('user')
passwd = UserInfo('pwd')

def login(driver):
    Login(driver).zentao().click()
    Login(driver).user().send_keys(username)
    Login(driver).password().send_keys(passwd+Keys.RETURN)
    time.sleep(5)