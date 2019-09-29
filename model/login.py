# coding=utf-8;
from pageproject.loginpage import login
from selenium.webdriver.support.ui import Select
import time

def login_step(driver):
    logins=login(driver)
    logins.root_id_input().send_keys('sty')
    logins.root_pwd_input().send_keys("123456aA")
    logins.denglu_click().click()
    logins.yonghu_click().click()
    logins.useradd_click().click()
    select1=Select(logins.bumen_click())
    select1.select_by_index(1)
    # select1.select_by_visible_text("/赵志航")
    # logins.root_click().send_keys("乃帝")
    select2=Select(logins.zhiwei_click())
    select2.select_by_visible_text('测试')
    time.sleep(10)