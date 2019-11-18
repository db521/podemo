from pageobject.loginPage import login

def longinstep(driver,name,password):
    try:
        logins = login(driver)
        logins.nameObj().send_keys(name)
        logins.passwordObj().send_keys(password)
        logins.btnObj().click()
    except Exception as e:
        raise e