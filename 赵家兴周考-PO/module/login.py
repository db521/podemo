from pageobject.LoginPage import Login
from time import sleep

def loginStep(driver,user,passwd):
    try:
        logins=Login(driver)
        logins.UserObj().send_keys(user)
        logins.PasswdObj().send_keys(passwd)
        logins.SubmitObj().click()
        sleep(2)
    except Exception as e:
        raise e

