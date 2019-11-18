#!/usr/bin/env python
# -*- coding: utf-8 -*-


from module.loginmdl import *
from selenium import webdriver
from utils.read_write import *
from time import *


class LoginTest(object):

    def __init__(self):  # 驱动浏览器，访问网址
        self.driver = webdriver.Firefox()
        self.driver.get(Read_Write().read_write("../config/urls.json")['url'])

    def logintest(self):  # 读取用户名密码，登录
        username = Read_Write().read_write("../config/usersandpasswd.json")['user']
        passwd = Read_Write().read_write("../config/usersandpasswd.json")['passwd']
        LoginStep().loginstep(self.driver, username, passwd)

    def __del__(self):  # 强制等待5秒后关闭浏览器
        sleep(5)
        self.driver.close()


if __name__ == '__main__':
    tlogin = LoginTest()
    tlogin.logintest()
