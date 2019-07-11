#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/30 17:26 
# @File : login.py
from selenium.webdriver.common.keys import Keys

from pageobject.loginPage import login
import time
def loginStep(driver, user, passwd,username,userpwd1,userpwd2,zname,email,cname):
    try:
        logins = login(driver)
        logins.buttonObj().click()
        time.sleep(5)
        logins.nameObj().send_keys(user)
        time.sleep(5)
        logins.passwdObj().send_keys(passwd)
        time.sleep(5)
        logins.aloginObj().click()
        logins.zuzhiObj().click()
        logins.adduserObj().click()
        logins.cliObj().click()
        logins.bumenObj().click()
        logins.namesObj().send_keys(username)
        logins.passwds1Obj().send_keys(userpwd1)
        logins.passwds2Obj().send_keys(userpwd2)
        logins.znameObj().send_keys(zname)
        logins.testObj().click()
        time.sleep(5)
        logins.emailObj().send_keys(email)
        logins.cnameObj().send_keys(cname)
        time.sleep(5)
        logins.registerObj().click()
        time.sleep(3)
        # 登陆操作
    except Exception as e:
        raise e
