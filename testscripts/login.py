#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/30 16:47 
# @File : login.py
import json

from module.login import loginStep,deptStep
from selenium import webdriver

def testloginZentao():
    """
    具体的测试流程，调用module模块的具体函数
    :return:
    """
    try:
        driver = webdriver.Chrome()
        # user=excel解析后的user值
        # pass=excel解析后的值
        with open("../config/config.json",'r')as f:
            data = json.loads(f.read())
            driver.get(url=data['url'])
            user = data['name']
            passwd = data['passwd']
        loginStep(driver, user, passwd)
        deptStep(driver,user)
    except Exception as e:
        raise e

testloginZentao()