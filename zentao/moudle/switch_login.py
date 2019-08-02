from pageobject.login import Login

def switch_Login(driver):

    try:

        logins = Login(driver)

        logins.buttonUser().click()

    except Exception as e:
        raise e

