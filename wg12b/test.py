from selenium import webdriver
from wg12b.util.wait import getElementImplicitWait as ge
from selenium.webdriver.common.keys import Keys

#进入网址
browser = webdriver.Chrome()
from wg12b.util.parsejson import parseurl as pu
url = pu('url')
browser.get(url)
# 点击“开源版”按钮
from wg12b.util.parsejson import parselocator as pl
zentao = pl("login","zentao")
property = zentao[0]
location = zentao[1]
elem = ge(browser,property,location)
elem.click()
#用户名
name = pl("login","name")
property = name[0]
location = name[1]
elem = ge(browser,property,location)
elem.send_keys('sty')
#密码
# name = pl("login","passwd")
# property = name[0]
# location = name[1]
# elem = ge(browser,property,location)
# elem.send_keys('123456aA' + Keys.ENTER)

# name = browser.find_element_by_id('account')
# name.send_keys('sty')
# passwd = browser.find_element_by_name('password')
# passwd.send_keys('123456aA' + Keys.ENTER)

