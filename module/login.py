#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/30 17:26 
# @File : login.py
from pageobject.loginPage import login
import time
from selenium.webdriver.common.keys import Keys


def loginStep(driver, user, passwd):
    try:
        logins = login(driver)
        logins.ztObj().click()
        logins.nameObj().send_keys(user)
        logins.passwdObj().send_keys(passwd+Keys.RETURN)
        logins.zuzhi().click()
        logins.adduser().click()
        logins.el_sel().click()
        logins.sel().click()
        logins.uname().send_keys('huawu')
        logins.password1().send_keys('131415aA~')
        logins.password2().send_keys('131415aA~')
        logins.realname().send_keys("李斌斌")
        logins.join().click()
        logins.data().click()
        logins.role().click()
        logins.top().click()
        logins.email().send_keys("l13546540911@126.com")
        logins.verifyPassword().send_keys("131415aA~")
        logins.submit().click()
        # time.sleep()
        # 登陆操作
    except Exception as e:
        raise e
