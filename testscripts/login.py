#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/2 14:58
# @Author  : 郭轩甫
# @Site    : 
# @File    : login.py
# @Software: PyCharm


import json

from module.login import loginStep
from selenium import webdriver

def testloginZentao():
    try:
        driver=webdriver.Chrome()
        with open('../config/config.json','r+') as f:
            w=json.loads(f.read())
        url=w['url']
        driver.get(url)
        loginStep(driver)
    except Exception as e:
        raise e

if __name__=='__main__':
    testloginZentao()
