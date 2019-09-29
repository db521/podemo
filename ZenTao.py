from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# import json
from util.parsejson import parseurl as pu
from util.parsejson import parselocation as pa
from util.util import getElementImplicitWait as gt
from util.parsejson import parseuser as pr

chrome = webdriver.Chrome()
url = pu("url")
chrome.get(url)
chrome.maximize_window()
zentao = pa("login", "zentao")
label = zentao[0]
attribute = zentao[1]
source = gt(chrome, label, attribute)
source.click()
user = pa("login", "name")
label = user[0]
attribute = user[1]
user = pr("user")
passwd = pr("pwd")
name = gt(chrome, label, attribute)
name.send_keys(user)
pwd = pa("login", "pwd")
label = pwd[0]
attribute = pwd[1]
pwd = gt(chrome, label, attribute)
pwd.send_keys(passwd + Keys.RETURN)
