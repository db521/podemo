from testscripts.login import *
from pageobject.login import Login_CD

def login_CD(driver,user,passwd):
    lg = Login_CD(driver)
    lg.userObj().clear()
    lg.userObj().send_keys(user)
    lg.passwdObj().clear()
    lg.passwdObj().send_keys(passwd)
    lg.login_btn().click()

