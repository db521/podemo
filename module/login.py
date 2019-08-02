from pageobject.loginPage import Login


def loginStep(driver):
    try:
        login = Login(driver)

        login.ver().click()
        login.useript().send_keys(login.userread())
        login.passwdipt().send_keys(login.passwdread())
        login.logbtn().click()

    except Exception as e:
        raise e