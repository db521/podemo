#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/30 17:26 
# @File : login.py
from selenium.webdriver.common.keys import Keys

from pageobject.loginPage import login

def loginStep(driver, user, passwd):
    try:
        logins = login(driver)
        logins.nameObj().send_keys(user)
        logins.passwdObj().send_keys(passwd + Keys.RETURN)
        # 登陆操作
    except Exception as e:
        raise e
