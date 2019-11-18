#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/30 17:26 
# @File : login.py
from pageobject.loginPage import login

import time
def loginStep(driver,name,passwd):
    try:
        logins = login(driver)
        time.sleep(2)
        logins.nameObj().send_keys(name)
        logins.passwdObj().send_keys(passwd)
        logins.btnObj().click()
        logins.zuzhiObj().click()
        logins.bumenObj().click()
        logins.yijibumen().click()

        # 登陆操作
    except Exception as e:
        raise e


def Addbumen(driver,Abumen):
    try:
        logins = login(driver)
        time.sleep(2)
        logins.erjibumen().click()
        logins.erjibumen().send_keys(Abumen)
        logins.addbaocun().click()
    except Exception as e:
        raise e

if __name__ == '__main__':
    from selenium import webdriver
    pass
