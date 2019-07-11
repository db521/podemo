#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/30 17:26 
# @File : login.py
from selenium.webdriver.common.keys import Keys

from pageobject.loginPage import login


def loginStep(driver, user, passwd, user2, pwd, cpwd, name, xpwd):
    try:
        logins = login(driver)
        logins.nameObj().send_keys(user)
        logins.passwdObj().send_keys(passwd)
        logins.bntObj().click()
        logins.zzObj().click()
        logins.yhObj().click()
        logins.seObj().click()
        logins.cObj().click()
        logins.cnameObj().send_keys(user2)
        logins.pwdObj().send_keys(pwd)
        logins.cpwdObj().send_keys(cpwd)
        logins.znamedObj().send_keys(name)
        logins.xpwddObj().send_keys(xpwd + Keys.RETURN)
        # 登陆操作
    except Exception as e:
        raise e
