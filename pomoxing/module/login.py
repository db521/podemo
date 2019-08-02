from pageobject.loginPage import login
def loginStep(driver):
    try:
        logins = login(driver)
        logins.nameObj().send_keys(logins.userRead())
        logins.passwdObj().send_keys(logins.pwdRead())
        logins.btnObj().click()
        logins.zuzhiObj().click()
        logins.addObj().click()
    except Exception as e:
        raise e
