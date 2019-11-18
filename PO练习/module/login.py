from pageobject.login import Login

def loginStep(driver,user,passwd):
    try:
        login = Login(driver)
        login.UserObj().send_keys(user)
        login.PasswdObj().send_keys(passwd)
        login.LoginObj().click()

    except Exception as e:
        raise e