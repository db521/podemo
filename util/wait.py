#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/4 19:42
# @Author  : 郭轩甫
# @Site    : 
# @File    : wait.py
# @Software: PyCharm

from selenium.webdriver.support.ui import WebDriverWait


def ElementWait(driver,locatType,locatelement):
    try:
        element=WebDriverWait(driver,30).until(lambda x:x.find_element(by=locatType,value=locatelement))
        return element
    except Exception as e:
        raise e
    pass
