#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019\7\8 0008 16:24 
# @File : test.py

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url='http://118.24.211.165:8081'
class ZentaoTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)


    def testPageTitle(self):
        # self.browser = webdriver.Chrome()
        self.browser.get(url)
        self.elem = self.browser.find_element_by_id('zentao')
        self.elem.click()
        self.name = self.browser.find_element_by_id('account')
        self.name.send_keys('admin')
        self.passwd = self.browser.find_element_by_name('password')
        self.passwd.send_keys('131415aA~' + Keys.RETURN)
        self.company = self.browser.find_element_by_link_text('组织')
        self.company.click()
        self.pri = self.browser.find_element_by_link_text('添加用户')
        self.pri.click()
        self.chosen = self.browser.find_element_by_class_name('chosen-single')
        self.chosen.click()
        # self.department = self.browser.find_element_by_css_selector('#dept_chosen > div > ul > li.active-result.result-selected')
        self.department = self.browser.find_element_by_xpath('//*[@id="dept_chosen"]/div/ul/li[2]')
        self.department.click()
        self.username = self.browser.find_element_by_name('account')
        self.username.send_keys('haoluqiang')
        self.pwd = self.browser.find_element_by_name('password1')
        self.pwd.send_keys('131415aA~')

        time.sleep(15)
        # self.options = self.browser.find_element_by_css_selector('options')
        # self.options.click()






if __name__ == '__main__':
    unittest.main(verbosity=2)
    suite=unittest.TestSuite()
    suite.addTest(ZentaoTestCase("testPageTitle"))
    suite.addTest(ZentaoTestCase("testPageTitle1"))
    suite.addTest(ZentaoTestCase("testPageTitle2"))
    suite.addTest(ZentaoTestCase("testPageTitle3"))
    # suite.addTest(ZentaoTestCase("testPageTitle4"))
    #可以顺序添加多个case,这样就可以顺序执行单元测试了

    runner=unittest.TextTestRunner()
    runner.run(suite)
