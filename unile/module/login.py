#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/30 17:26 
# @File : login.py
from pageobject.loginPage import login
import time
from selenium.webdriver.common.keys import Keys

def loginStep(driver,name,passwd,bumen):
    try:
        logins = login(driver)
        logins.nameObj().send_keys(name)
        logins.passwdObj().send_keys(passwd)
        time.sleep(3)
        logins.btnObj().click()
        time.sleep(3)
        logins.addObj().click()
        logins.bumenObj().send_keys(bumen+Keys.ENTER)
        time.sleep(3)

        # 登陆操作
    except Exception as e:
        raise e

# if __name__ == '__main__':
# #     pass