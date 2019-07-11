#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/30 17:26 
# @File : login.py
from pageobject.loginPage import login
import json




def loginStep(driver):
    with open('../config/userpwd.json', 'r+', encoding='utf-8') as file:
        aa = json.loads(file.read())
        user = aa['login']['name']
        passwd = aa['login']['passwd']
        try:
            logins = login(driver)
            logins.nameObj().send_keys(user)
            logins.passwdObj().send_keys(passwd)

        except Exception as e:
            raise e



