#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/6/30 16:47 
# @File : login.py
import json

from module.login import loginStep,login22
from selenium import webdriver
import time

def testloginZentao():
    """
    具体的测试流程，调用module模块的具体函数
    :return:
    """
    try:
        driver = webdriver.Chrome()
        # user=excel解析后的user值
        # pass=excel解析后的值
        with open('E:\郭亚光\pycham的\python文件\podemo\config\config.json','r') as f:
            url = json.loads(f.read())['url']
            print(url)
        driver.get(url=url)
        with open('E:\郭亚光\pycham的\python文件\podemo\config\puser.json','r') as fi:
            # print(fi)
            Admin = json.loads(fi.read())['guoyaguang888']
            user = Admin[0]
            passwd=Admin[1]
        loginStep(driver,user,passwd)
        time.sleep(3)
        login22(driver)
    except Exception as e:
        raise e

if __name__ == '__main__':
    testloginZentao()