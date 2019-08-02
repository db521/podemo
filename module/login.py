#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/30 17:26 
# @File : login.py
from pageobject.loginPage import login


def loginStep(driver):
    try:
        logins = login(driver)

        logins.nameObj().send_keys(logins.userRead())
        logins.passwdObj().send_keys(logins.pwdRead())
        logins.btnObj().click()
        logins.zuzhiObj().click()
        logins.addObj().click()
        # 登陆操作
    except Exception as e:
        raise e
