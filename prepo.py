# -*- coding: utf-8 -*-
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# url='http://94.191.28.11/'
# ch=webdriver.Chrome()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

bs=webdriver.Chrome()
from util.parsejson import parseurl as pu
from util.parsejson import parselocator as pl
url=pu("url")#
bs.get(url)

from util.util import getElementImplicitWait as ge
zentao=pl("login","zentao")
strategy=zentao[0]
locator=zentao[1]
elem=ge(bs,strategy,locator)
elem.click()


name = bs.find_element_by_id('account')
name.send_keys('sty')
passwd = bs.find_element_by_name('password')
passwd.send_keys('123456aA' + Keys.RETURN)