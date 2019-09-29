import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

bs=webdriver.Chrome()
from util.parsejson import parseurl as pu
from util.parsejson import parselocator as pl
url=pu("url")
bs.get(url)

from util.util import getElementImplicitwait as ge
zentao=pl("login","zentao")
strategy=zentao[0]
locator=zentao[1]
elem=ge(bs,strategy,locator)
elem.click()
from util.parsejson import parseloginuser
from util.parsejson import parseloginpwd
user=parseloginuser("user")
pwd=parseloginpwd("pwd")
name = bs.find_element_by_id('account')
name.send_keys(user)
passwd = bs.find_element_by_name('password')
passwd.send_keys(pwd + Keys.RETURN)