#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/30 17:26 
# @File : login.py
from pageobject.loginPage import login
import time


def loginStep(driver, user, passwd):
    try:
        logins = login(driver)
        logins.nameObj().send_keys(user)
        logins.passwdObj().send_keys(passwd)
        logins.btnObj().click()
        time.sleep(3)
        # 登陆操作
    except Exception as e:
        raise e

def deptStep(driver,user):
    try:
        dept = login(driver)
        dept.zuzhiObj().click()
        dept.zuzhiwhObj().click()
        dept.deptnameObj().send_keys(user)
        dept.btnObj().click()
        # dept.deptlistObj().click()
        time.sleep(5)
        # 登陆操作
    except Exception as e:
        raise e
