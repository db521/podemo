#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/30 17:01 
# @File : loginPage.py
import json
from util.obj import obj
from util.open_file import open_file
class login:
    def __init__(self, driver):
        self.driver = driver
        self.sw=open_file('pageobject')
    def nameObj(self):  # 单个元素的获取方法
        try:
            return obj(self.driver, self.sw, 'login', 'name')
        except Exception as e:
            raise e

    def passwdObj(self):  # 单个元素的获取方法
        try:
            return obj(self.driver, self.sw, 'login', 'passwd')
        except Exception as e:
            raise e

    def btnObj(self):  # 单个元素的获取方法
        try:
            return obj(self.driver, self.sw, 'login', 'btn')
        except Exception as e:
            raise e
