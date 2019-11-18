from pageobj.login_Page import ligin
from utils.key import *

def addStep(driver,bumen_name):
    try:
        adds=ligin(driver)
        adds.zuzhiObj().click()
        adds.bumenObj().click()
        adds.addbmObj().send_keys(bumen_name+Keys_Enter())


    except Exception as e:
        raise e
