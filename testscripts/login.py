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
        driver = webdriver.Chrome()
        # user=excel解析后的user值
        # pass=excel解析后的值
        with open(r'C:\Users\闫学谦\Desktop\podemo\config\config.json')as f:
            uq = json.loads(f.read())['url']
        driver.get(uq)
        with open(r'C:\Users\闫学谦\Desktop\podemo\config\register.json')as f1:
            uw = json.loads(f1.read())
        user=uw['user']
        passwd=uw['passwd']
        loginStep(driver, user, passwd)
    except Exception as e:
        raise e

if __name__ == '__main__':
    testloginZentao()

