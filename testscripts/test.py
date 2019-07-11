#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019\7\8 0008 16:24 
# @File : test.py

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

url='http://118.24.211.165:8081'
class ZentaoTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get(url)
        self.elem = self.browser.find_element_by_id('zentao')
        self.elem.click()

        self.zuzhi = self.browser.find_element_by_xpath('//*[@id="navbar"]/ul/li[9]/a').click()
        self.bumen = self.browser.find_element_by_xpath('//*[@id="subNavbar"]/ul/li[2]/a').click()

        sleep(10)

if __name__ == '__main__':
    unittest.main(verbosity=2)
    suite=unittest.TestSuite()
    suite.addTest(ZentaoTestCase("testPageTitle"))
    suite.addTest(ZentaoTestCase("testPageTitle1"))
    suite.addTest(ZentaoTestCase("testPageTitle2"))
    suite.addTest(ZentaoTestCase("testPageTitle3"))
    #可以顺序添加多个case,这样就可以顺序执行单元测试了
    runner=unittest.TextTestRunner()
    runner.run(suite)
