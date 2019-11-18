from pageobject.AddPage import Add
from time import sleep
from util.Key import *

def addStep(driver,bumen):
    try:
        adds=Add(driver)
        adds.ZuzhiObj().click()
        adds.BumenObj().click()
        adds.AddObj().send_keys(bumen+Key_Enter())
        sleep(2)
    except Exception as e:
        raise e

