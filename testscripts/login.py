#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/30 16:47 
# @File : login.py
import json

from module.login import loginStep
from selenium import webdriver


def atestloginZentao():
    """
    具体的测试流程，调用module模块的具体函数
    :return:
    """
    try:
        driver = webdriver.Chrome()
        driver.maximize_window()
        # user=excel解析后的user值
        # pass=excel解析后的值
        with open('../config/config.json',mode="r")as f:
            w = json.loads(f.read())
        url=w['url']
        driver.get(url)
        user='admin'
        passwd='131415aA~'
        loginStep(driver, user, passwd)
    except Exception as e:
        raise e
if __name__ == '__main__':
    atestloginZentao()