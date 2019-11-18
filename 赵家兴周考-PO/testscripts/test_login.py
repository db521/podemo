from util.Try_Test import *
from module.login import loginStep
from selenium import webdriver
def Test_Login():
    try:
        driver=webdriver.Chrome()
        driver.maximize_window()

        w=Try_Test("../config/url.json")
        driver.get(w['url'])

        w=Try_Test("../config/user.json")
        loginStep(driver,w['user'],w['passwd'])

    except Exception as e:
        raise e


if __name__ == '__main__':
    Test_Login()
