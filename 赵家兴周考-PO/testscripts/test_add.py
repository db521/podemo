from util.Try_Test import *
from module.add import addStep
from selenium import webdriver
def Test_Add():
    try:
        driver=webdriver.Chrome()
        driver.maximize_window()


        w=Try_Test("../config/add.json")
        addStep(driver,w['bumen'])

    except Exception as e:
        raise e


if __name__ == '__main__':
    Test_Login()
