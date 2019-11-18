from util.Try_Test import *
from module.delete import delStep
from selenium import webdriver
def Test_Del():
    try:
        driver=webdriver.Chrome()
        driver.maximize_window()

        delStep(driver)

    except Exception as e:
        raise e


if __name__ == '__main__':
    Test_Login()
