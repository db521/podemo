#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/30 17:26 
# @File : login.py
from pageobject.loginPage import login
import time

def loginStep(driver, user, passwd):
    try:
        logins = login(driver)
        logins.loginObj().click()
        logins.nameObj().send_keys(user)
        logins.passwdObj().send_keys(passwd)
        logins.submitObj().click()
        logins.zuzhiObj().click()
        logins.addnameObj().click()
        logins.listsObj().click()
        logins.listlObj().click()
        logins.usernameObj().send_keys("xiaoxiao")
        logins.passwd1Obj().send_keys("123456.wp")
        logins.passwd2Obj().send_keys("123456.wp")
        logins.realnameObj().send_keys("王鹏")
        logins.positionObj().click()
        logins.emailObj().send_keys("daniel52121@163.com")
        logins.verifypasswordObj().send_keys("131415aA~")
        logins.dianjiObj().click()

        time.sleep(5)
        # 登陆操作
    except Exception as e:
        raise e
