#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/5 9:13
# @Author  : 郭轩甫
# @Site    : 
# @File    : login.py
# @Software: PyCharm


import json
from module.login import loginStep
from selenium import webdriver

def testloginzentao():
    try:
        driver=webdriver.Chrome()
        with open('../config/config.json','r+') as f:
            url=json.loads(f.read())
        url1=url['url']
        driver.get(url1)
        loginStep(driver)

    except Exception as e:
        raise e

if __name__=='__main__':

    testloginzentao()