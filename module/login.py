#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/2 14:05
# @Author  : 郭轩甫
# @Site    : 
# @File    : login.py
# @Software: PyCharm

from pageobject.loginpage import login

def loginStep(driver):
    try:
        logins=login(driver)
        logins.zenObj().click()
        logins.nameObj().send_keys(logins.userRead())
        logins.passwordObj().send_keys(logins.pwdRead())
        logins.btnObj().click()
        logins.zuzhiObj().click()
        logins.addObj().click()
    except Exception as e:
        raise e