# -*- coding: utf-8 -*-
from po.login import Login
def login(driver):
    Login(driver).zentao().click()
    Login(driver).user().send_keys('d')
    Login(driver).passwd()


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    login(driver=driver)