from pagelogin.logins import Login

def LoginSetup(driver,name,passwd):
    try:
        logins = Login(driver)
        logins.nameobj().send_keys(name)
        logins.passwdobj().send_keys(passwd)
        logins.buttenobj().click()

    except Exception as e:
        raise e