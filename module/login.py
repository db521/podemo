from pageobject.loginPage import login
import time
def loginStep(driver):
    try:
        logins=login(driver)
        logins.btnObj().click()
        logins.nameObj().send_keys(logins.userRead())
        logins.passwdObj().send_keys(logins.pwdRead())
        logins.btn1Obj().click()
        time.sleep(10)


    except Exception as e:
        raise e
