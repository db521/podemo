#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/30 17:26 
# @File : login.py
from pageobject.loginPage import login,login2
import time
from selenium.webdriver.common.keys import Keys

def loginStep(driver, user, passwd):
    try:
        logins = login(driver)
        logins.nameObj().send_keys(user)
        logins.passwdObj().send_keys(passwd + Keys.RETURN)
        # 登陆操作
        time.sleep(3)

    except Exception as e:
        raise e

def login22(driver):
    try:
        logins = login2(driver)
        logins.zuzhiObj().click()
        logins.tianjiaObj().click()
        logins.selectObj().click()
        logins.select2Obj().click()
        time.sleep(10)

    except Exception as e:
        raise e
