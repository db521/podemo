from pageobject.DelPage import Del
from time import sleep
from util.Alert import *

def delStep(driver):
    try:
        dels=Del(driver)
        dels.DelObj().click()
        alert_accept(driver)
        sleep(2)
    except Exception as e:
        raise e

