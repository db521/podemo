#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/30 16:47 
# @File : loginz.py
import json

from module.login import loginStep
from selenium import webdriver


def testloginZentao():
    """
    登陆页面，获取用户名和密码，是通过excel文件解析
    页面的所有元素定义在pageobject文件夹下面的loginPage里面
    所有的定位方式在config里面的pageobject里面
    这个页面就是综合调用一下
    :return:
    """
    try:
        driver = webdriver.Chrome()
        # user=excel解析后的user值
        # pass=excel解析后的值
        driver.get(url=json.loads('./config/config.json')['url'])
        user=''
        passwd=''
        loginStep(driver, user, passwd)
    except Exception as e:
        raise e
