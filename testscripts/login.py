#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/30 16:47 
# @File : login.py
import json

from module.login import loginStep
from selenium import webdriver
from pageobject.loginPage import  login


def testloginZentao():
    """
    具体的测试流程，调用module模块的具体函数
    :return:
    """
    try:
        driver = webdriver.Chrome()
        # user=excel解析后的user值
        # pass=excel解析后的值
        # driver.get(url=json.loads('./config/config.json')['url'])
        with open('../config/config.json', mode='r') as f:
            ww = json.loads(f.read())
            url = ww['url']
            driver.get(url)
        with open('../config/passwd.json', mode='r') as a:
            zz = json.loads(a.read())
        user = zz["login1"]["user"]
        passwd = zz["login1"]["passwd"]
        loginStep(driver, user, passwd)
    except Exception as e:
        raise e


if __name__ == '__main__':
    testloginZentao()
