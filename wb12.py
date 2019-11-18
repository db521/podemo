from selenium import webdriver
url='http://127.0.0.1/biz/user-login-L2Jpei8=.html'
from selenium.webdriver.common.keys import Keys

bs=webdriver.Chrome()
bs.get(url)
assert '禅道' in bs.title

elem = bs.find_element_by_id('zentao')
elem.click()
name = bs.find_element_by_id('account')
name.send_keys('sty')
passwd = bs.find_element_by_name('password')
passwd.send_keys('123456aA' + Keys.RETURN)