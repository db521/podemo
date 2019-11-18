#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/30 16:47 
# @File : login.py
import json

from module.login import loginStep
from module.ajkk import Addbumen
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time

def testloginZentao():
    """
    具体的测试流程，调用module模块的具体函数
    :return:
    """
    try:
        driver = webdriver.Chrome()
        # user=excel解析后的user值
        # pass=excel解析后的值
        with open('../config/urls.json','r')as f:
            w=json.loads(f.read())
        url = w['url']
        driver.get(url)
        with open('../config/add.json','r') as f:
            ad = json.loads(f.read())
        ejk = ad["addbm"]
        with open('../config/user.json','r') as f:
            us = json.loads(f.read())
        name = us['user']
        passwd = us['passwd']
        loginStep(driver,name,passwd)
        Addbumen(driver,ejk)

        # newuser(driver,"zhangsan","123456")
        time.sleep(5)

    except Exception as e:
        raise e

if __name__ == '__main__':
    testloginZentao()
