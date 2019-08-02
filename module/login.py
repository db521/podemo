# -*- coding: utf-8 -*-
# import vie,ser,oth,mod,url

from pageobject.loginpage import login

def loginStep(driver):
    try:
        logins = login(driver)
        logins.btnobj().click()
        logins.useobj().send_keys(logins.use_value())
        logins.passwdobj().send_keys(logins.passwd_value())
        logins.loginobj().click()

    except Exception as e:
        raise e
