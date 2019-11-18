from pageobjects.loginpage import login
from util.keys import *
import time
def loginStep(driver,user,passwd):
    try:
        logins=login(driver)
        time.sleep(3)
        logins.userObj().send_keys(user)
        time.sleep(3)
        logins.passwdObj().send_keys(passwd+Key_Enter())
        time.sleep(3)
        # logins.btnObj().click()
        # time.sleep(4)
    except Exception as e:
        raise e


