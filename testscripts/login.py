#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/30 16:47 
# @File : login.py
import json
import time
from module.login import loginStep
from selenium import webdriver
from pageobject.loginPage import login


def loginZentao():
    """
    具体的测试流程，调用module模块的具体函数
    :return:
    """
    try:
        driver = webdriver.Chrome()
        exam = login(driver)
        url = exam.urlObj()
        user = exam.userObj()
        passwd = exam.pwdObj()



        driver.get(url)
        loginStep(driver, user, passwd)
        time.sleep(15)
    except Exception as e:
        raise e

if __name__ == '__main__':
    loginZentao()