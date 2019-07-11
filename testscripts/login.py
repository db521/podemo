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
        with open("../config/config.json", 'r') as file:
            url = json.loads(file.read())
        aa = url["url"]
        driver.get(aa)
        with open("../config/pageobject.json", 'r')as f:
            ss = json.loads(f.read())
            # print(ss)
        use = ss["login"]["account"]
        user = use[2]
        pwd = ss["login"]["password"]
        passwd = pwd[2]
        # user='admin'
        # passwd='131415aA~'
        loginStep(driver, user, passwd)
    except Exception as e:
        raise e


if __name__ == '__main__':
    testloginZentao()
