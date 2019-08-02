#coding=utf-8;
from pageproject.loginPage import login
import time
def login_step(driver):
    logins=login(driver)
    time.sleep(1)
    logins.zdbtn_click().click()
    time.sleep(1)
    logins.root_id_inut().send_keys('B1611')
    logins.root_pwd_inut().send_keys("123456aA")
    logins.denglu_click().click()
    logins.zuzhi_click().click()
    logins.bumen_click().click()
    logins.sty_click().click()
    time.sleep(1)