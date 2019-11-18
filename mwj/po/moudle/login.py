from pageobj.login_Page import ligin
import time
from utils.alter import Alter

from selenium.webdriver.common.keys import Keys

def loginsUp(driver,name,passwd,bumen):

    try:

        logins = ligin(driver)
        logins.nameObj().send_keys(name)
        logins.passwdObj().send_keys(passwd)
        logins.btnObj().click()
        logins.useObj().click()
        logins.zhutiObj()
        logins.besObj().click()
        time.sleep(3)
        logins.zuzhiObj().click()
        logins.bumenObj().click()
        logins.addbmObj().send_keys(bumen+Keys.ENTER)
        time.sleep(3)
        logins.delsObj().click()
        Alter(driver)
        time.sleep(2)

    except Exception as e:
        raise e