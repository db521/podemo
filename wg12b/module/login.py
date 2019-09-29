from wg12b.pageobject.login import Login
from selenium import webdriver
import time

def login():
    driver = webdriver.Chrome()
    login = Login(driver)
    login.deng()
    login.zentao()
    login.name()
    login.passwd()
    time.sleep(3)
if __name__ == '__main__':
    login()




