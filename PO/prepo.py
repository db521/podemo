# -*- coding: utf-8 -*-
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
bs = webdriver.Chrome()
from util.parsejson import parseurl as pu
from util.parsejson import parselocator as pl
url = pu("url")
bs.get(url)
#with open(r"./config/url.json", 'r') as f:
#     content = json.loads(f.read())
# from util.parsejson import parsejson as pj
# content2 = pj(r"./config/url.json")
# try:
#     url = content2["url"]
# except Exception as e:
#     print(e)
# bs.get(url)
# assert '禅道' in bs.title
# elem = bs.find_element_by_id('zentao')
from util.util import getElementImplicitWait as ge
# with open(r".\config\map.json", 'r') as f:
#     content1 = json.loads(f.read())
zentao = pl("login","zentao")
strategy = zentao[0]
locator = zentao[1]
print(zentao)
elem =ge(bs,strategy,locator)
elem.click()
name = bs.find_element_by_id('account')
name.send_keys('sty')
passwd = bs.find_element_by_name('password')
passwd.send_keys('123456aA' + Keys.RETURN)

