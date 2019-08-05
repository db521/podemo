from selenium import webdriver

from pageobjects.loginpage import login
import time


def loginclick(driver):
    logins = login(driver)
    logins.kaiyuan().click()
    logins.userr().send_keys(logins.userinput())
    logins.passwd().send_keys(logins.passwordinput())
    logins.loginclick().click()
    logins.zu().click()
    logins.bu().click()
    logins.song().click()
    logins.zeng().send_keys(logins.bumeninput())
    logins.busmb().click()


    time.sleep(10)



