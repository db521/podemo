#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/30 17:26 
# @File : login.py
from pageobject.loginPage import login
import time


def loginStep(driver, user, passwd):
    try:
        logins = login(driver)
        logins.buttonObj().click()
        time.sleep(3)
        logins.userObj().send_keys(user)
        logins.pwdObj().send_keys(passwd)
        logins.loginsObj().click()
        time.sleep(3)
        # 登陆操作
    except Exception as e:
        raise e


