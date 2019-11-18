#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/30 16:47 
# @File : login.py
import json

from module.login import loginStep,Addbumen
from selenium import webdriver


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

        with open('../config/addbumen.json','r')as f:
            bumen=json.loads(f.read())
        Abumen = bumen['shuru']

        time.sleep(3)

        with open('../config/user.json','r')as f:
            pswd=json.loads(f.read())
        user = pswd['user']
        passwd = pswd['passwd']
        loginStep(driver,user,passwd)
        Addbumen(driver,Abumen)
        # newuser(driver,"zhangsan","123456")



        time.sleep(3)


    except Exception as e:
        raise e

if __name__ == '__main__':
    testloginZentao()
