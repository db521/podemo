#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/30 17:26 
# @File : login.py
from pageobject.loginPage import login


def loginStep(driver, user, passwd):
    try:
        logins = login(driver)
        logins.nameObj().click()
        logins.nameObj().send_keys(user)
        logins.passwdObj().send_keys(passwd)
        # 登陆操作
    except Exception as e:
        raise e



# if __name__ == '__main__':
#     from selenium import webdriver
#     dri = webdriver.Chrome()
#     import json
#     with open('../config/passwd.json', mode='r') as f:
#         zz = json.loads(f.read())
#         print(zz)
#     user = zz["login1"]["user"]
#     passwd = zz["login1"]["passwd"]
#     loginStep(dri,user,passwd)

