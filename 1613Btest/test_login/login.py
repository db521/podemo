# -*- coding: utf-8 -*-
'''
@Time    : 2019/9/28 8:56
@Author  : Allen
@File    : .py
'''
from selenium import webdriver
from tools.parsejson import parseurl as pu
from tools.parsejson import parse_anniu as an
from tools.parsejson import Userinfo as us
from tools.util import *
class
driver = webdriver.Chrome()
url = pu("url")
website(driver,url)

from tools.util import getElementImplicitWait as shi
# from tools.util import getElementImplicitWait
zentao = an(r'../config/dingwei.json',"login","zentao")
ding_type = zentao[0]
ding_zhi = zentao[1]
elem = shi(driver,ding_type,ding_zhi)
elem.click()


# ========================定位用户======================================
user = an(r'../config/dingwei.json',"login","account")
ding_type1 = user[0]
ding_zhi1 = user[1]
elem = shi(driver,ding_type1,ding_zhi1)
key = us(r'../config/user.json',"name")
elem.send_keys(key)


# ========================定位密码======================================
# passwd = an(r'../config/dingwei.json',"login","password")
# ding_type2 = passwd[0]
# ding_zhi2 = passwd[1]
#
#
driver.find_element_by_name('password').send_keys('123456aA')
driver.find_element_by_id('submit').click()


