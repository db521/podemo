#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/30 16:47 
# @File : test_login.py
from util.open_file import open_file
from module.login import loginStep
from selenium import webdriver

class Test_login:
    def __init__(self):
        self.driver = webdriver.Chrome()
    def testloginZentao(self):
        """
        具体的测试流程，调用module模块的具体函数
        :return:
        """
        try:
            w=open_file('urls')
            self.driver.get(w['url'])
            s=open_file('user')
            x = open_file('bumen')
            loginStep(self.driver,s['user'],s['passwd'])
        except Exception as e:
            raise e

if __name__ == '__main__':
    login=Test_login()
    login.testloginZentao()