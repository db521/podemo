from pageobject.loginpage import login
import time

def loginStep(driver,name,passwd):
    try:
        logins=login(driver)
        logins.nameObj().send_keys(name)
        logins.passwdObj().send_keys(passwd)
        logins.btnObj().click()
        time.sleep(3)

    except Exception as e:
        raise e

