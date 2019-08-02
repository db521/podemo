#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019\7\8 0008 16:24 
# @File : test.py
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
url='http://118.24.211.165:8081'
class ZentaoTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get(url)
        self.elem = self.browser.find_element_by_id('zentao')
        self.elem.click()
        self.name = self.browser.find_element_by_id('account')
        self.name.send_keys('admin')
        self.passwd = self.browser.find_element_by_name('password')
        self.passwd.send_keys('131415aA~' + Keys.RETURN)
        time.sleep(10)
    def testPageTitle1(self):
        self.browser.get(url)
        self.elem = self.browser.find_element_by_id('zentao')
        self.elem.click()
        self.name = self.browser.find_element_by_id('account')
        self.name.send_keys('admin')
        self.passwd = self.browser.find_element_by_name('password')
        self.passwd.send_keys('131415aA~' + Keys.RETURN)
        time.sleep(1)
        self.browser.find_element_by_link_text('组织').click()
        self.browser.find_element_by_partial_link_text('添加用户').click()
        from selenium.webdriver.support.ui import Select
        # 或者直接遍历父元素再直接for循环遍历查找
        select = Select(self.browser.find_element_by_id('dept'))
        select.select_by_visible_text('/1610C')
        time.sleep(10)
if __name__ == '__main__':
    unittest.main(verbosity=2)
    suite=unittest.TestSuite()
    suite.addTest(ZentaoTestCase("testPageTitle1"))
    #可以顺序添加多个case,这样就可以顺序执行单元测试了
    runner=unittest.TextTestRunner()
    runner.run(suite)
