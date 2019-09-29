# -*- coding: utf-8 -*-
from selenium import webdriver
import time

ch = webdriver.Chrome()
ch.maximize_window()
ch.implicitly_wait(10)
ch.get('https://www.baidu.com/')
ch.find_element_by_id('kw').send_keys('八维')
# ch.find_element_by_xpath('//*[@id="kw"]').send_keys('八维')
ch.find_element_by_id('su').click()


