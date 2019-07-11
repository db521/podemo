#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/30 16:47 
# @File : login.py
import json

from module.login import loginStep
from selenium import webdriver
from time import sleep


def testloginZentao():

    """
    具体的测试流程，调用module模块的具体函数
    :return:
    """
    try:
        driver = webdriver.Chrome()
        with open('../config/config.json',mode='r') as f:
            ss = json.loads(f.read())['url']

        # user=excel解析后的user值
        # pass=excel解析后的值
        driver.get(ss)
        with open(r'C:\Users\Administrator\Desktop\pod\podemo\config\register.json',mode='r') as f1:
            aa = json.loads(f1.read())
        user = aa['user']
        passwd = aa['passwd']
        loginStep(driver, user, passwd)
        sleep(3)
    except Exception as e:
        raise e


if __name__ == '__main__':
    testloginZentao()