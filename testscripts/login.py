#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/30 16:47 
# @File : login.py
import json

from module.login import loginStep
from selenium import webdriver


def testloginZentao():
    """
    具体的测试流程，调用module模块的具体函数
    :return:
    """
    try:
        with open('../config/config.json',mode='r') as f:
            ss = json.loads(f.read())['url']
        driver = webdriver.Chrome()
        # user=excel解析后的user值
        # pass=excel解析后的值
        driver.get(url=ss)
        with open('../config/config.json',mode='r') as f:
            aa = json.loads(f.read())
        user=aa['user']
        passwd=aa['password']
        username = aa['username']
        userpwd1 = aa['passwds1']
        userpwd2 = aa['passwds2']
        zname = aa['zname']
        email = aa['email']
        cname = aa['cname']
        loginStep(driver, user, passwd,username,userpwd1,userpwd2,zname,email,cname)
    except Exception as e:
        raise e



testloginZentao()