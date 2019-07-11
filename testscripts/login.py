#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/30 16:47 
# @File : login.py
import json
from time import sleep

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
        with open(r'C:\Users\10953\Desktop\daiam\podemo\config\config.json', mode='r')as f:
            u = json.loads(f.read())['url']
        url = u
        driver.get(url)
        with open(r'C:\Users\10953\Desktop\daiam\podemo\config\usespwd', mode='r')as f1:
            up = json.loads(f1.read())
        print(up)

        user = up['user']
        passwd = up['password']

        with open(r'C:\Users\10953\Desktop\daiam\podemo\config\add', mode='rb')as f2:
            ad = json.loads(f2.read())
        print(ad)
        user2 = ad['user']
        pwd = ad['pwd']
        cpwd = ad['cpwd']
        name = ad['name']
        xpwd = ad['xpwd']
        loginStep(driver, user, passwd, user2, pwd, cpwd, name, xpwd)
        sleep(3)
    except Exception as e:
        raise e


if __name__ == '__main__':
    testloginZentao()
