from time import sleep
from moudle.login import LoginStep
from selenium import webdriver
from untils.try_test import Try_Test

def test_login():

    driver = webdriver.Chrome()
    w = Try_Test("../config/url.json")
    driver.get(w['url'])
    w = Try_Test("../config/user.json")
    LoginStep(driver,w['user'],w['passwd'])
    sleep(2)


if __name__ == '__main__':
    test_login()
