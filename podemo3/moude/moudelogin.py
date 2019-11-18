from packmode.loginmode import login
import time
from selenium import webdriver

def logins(web,name,passwd):
    try:

        abc = login(web)
        abc.nameobj().send_keys(name)
        abc.passwdobj().send_keys(passwd)
        abc.clickobj().click()
        time.sleep(10)
    except Exception as e:
        raise e


