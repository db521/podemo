#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/4 19:40
# @Author  : 郭轩甫
# @Site    : 
# @File    : login.py
# @Software: PyCharm

from pageobject.loginpage import login
def loginStep(driver):
    try:
        logins=login(driver)
        logins.zenObg().click()
        logins.nameObg().send_keys(logins.userRead())
        logins.passwordObg().send_keys(logins.passwordRead())
        logins.btnObg().click()
        logins.zuzhiObg().click()
        logins.addObg().click()
    except Exception as e:
        raise e