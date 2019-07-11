import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

url = 'http://118.24.211.165:8081'


class ZentaoTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        # self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get(url)
        self.elem = self.browser.find_element_by_id('zentao')  # 开源版
        self.elem.click()  # 点击
        self.name = self.browser.find_element_by_id('account')  # 用户名输入框
        self.name.send_keys('admin')  # 输入用户名
        self.passwd = self.browser.find_element_by_name('password')  # 密码框
        self.passwd.send_keys('131415aA~' + Keys.RETURN)  # 输入密码
        self.organize = self.browser.find_element_by_css_selector('#navbar > ul > li:nth-child(9) > a')
        self.organize.click()
        self.adduser = self.browser.find_element_by_css_selector('#mainMenu > div.btn-toolbar.pull-right > a.btn.btn-primary')
        self.adduser.click()
        # self.input_box = self.browser.find_element_by_css_selector('#dept_chosen > a > div:nth-child(2) > b')
        # self.input_box.click()
        time.sleep(3)
        self.browser.find_element_by_class_name('chosen-single').click()
        # self.browser.find_element_by_xpath('//*[@id="dept_chosen"]/div/ul/li[2]').click()
        self.browser.find_element_by_css_selector('#dept_chosen > div > ul > li:nth-child(2)').click()
        # time.sleep(3)
        self.browser.find_element_by_css_selector('#account').send_keys('zihang')
        self.browser.find_element_by_css_selector('#password1').send_keys('pengzihang123')
        self.browser.find_element_by_css_selector('#password2').send_keys('pengzihang123')
        self.browser.find_element_by_css_selector('#realname').send_keys('彭自航')
        self.browser.find_element_by_css_selector('#role').click()
        self.browser.find_element_by_css_selector('#role > option:nth-child(3)').click()
        self.browser.find_element_by_xpath('//*[@id="group_chosen"]/a').click()
        self.browser.find_element_by_css_selector('#group_chosen > div > ul > li:nth-child(3)').click()
        self.browser.find_element_by_css_selector('#email').send_keys('pzh317997486@126.com')
        self.browser.find_element_by_css_selector('#commiter').send_keys('admin')
        self.browser.find_element_by_css_selector('#verifyPassword').send_keys('131415aA~')
        self.browser.find_element_by_css_selector('#submit').click()
        time.sleep(3)



if __name__ == '__main__':
    unittest.main(verbosity=2)
    suite = unittest.TestSuite()  # 测试套装对象
    suite.addTest(ZentaoTestCase('testPageTitle'))
    # suite.addTest(ZentaoTestCase('testPageTitle1'))
    # suite.addTest(ZentaoTestCase('testPageTitle2'))
    # suite.addTest(ZentaoTestCase('testPageTitle3'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
