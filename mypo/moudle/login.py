from pageobject.loginobj import *
from util.method import open_file
def logining(driver,name,passwd):
    try:
        file=open_file('paheobj.json')
        user_obj(driver,file).send_keys(name)
        passwd_obj(driver,file).send_keys(passwd)
        submit_obj(driver,file).click()
    except Exception as e:
        raise e
