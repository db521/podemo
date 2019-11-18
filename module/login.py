#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/30 17:26 
# @File : login.py
from pageobject.loginPage import login


def loginStep(driver,name,passwd):
    try:
        logins = login(driver)
        logins.nameObj().send_keys(name)
        logins.passwdObj().send_keys(passwd)
        logins.btnObj().click()



        # 登陆操作
    except Exception as e:
        raise e

if __name__ == '__main__':
    # from selenium import webdriver
    # driver = webdriver.Chrome()
    # driver.get("http://127.0.0.1/biz/user-login-L2Jpei8=.html")
    # loginStep(driver,"admin","yao123456")
    pass