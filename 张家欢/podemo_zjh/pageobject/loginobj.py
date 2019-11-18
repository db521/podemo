#!/usr/bin/env python
# -*- coding: utf-8 -*-


from utils.wait import *
from utils.read_write import *


class Login(object):  # 元素定位

    def __init__(self, driver01):
        self.driver01 = driver01

    def uelementfunction(self):  # 定位用户名输入框
        try:
            datadict = (Read_Write().read_write('../config/elements.json'))['uelement']
            locateProperty = datadict[0]
            locateValue = datadict[1]
            elements = ExplicitWait().explicitWait(self.driver01, locateProperty, locateValue)

            return elements

        except Exception as ep:
            raise ep

    def pelementfunction(self):  # 定位密码输入框
        try:
            datadict = (Read_Write().read_write('../config/elements.json'))['pelement']
            locateProperty = datadict[0]
            locateValue = datadict[1]
            elements = ExplicitWait().explicitWait(self.driver01, locateProperty, locateValue)

            return elements

        except Exception as ep:
            raise ep

    def sbelementfunction(self):  # 定位登录按钮
        try:
            datadict = (Read_Write().read_write('../config/elements.json'))['sbelement']
            locateProperty = datadict[0]
            locateValue = datadict[1]
            elements = ExplicitWait().explicitWait(self.driver01, locateProperty, locateValue)

            return elements

        except Exception as ep:
            raise ep
