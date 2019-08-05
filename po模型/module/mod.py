from pageobjects.logins import login
import time

def loginStep(driver):
    try:
        logins = login(driver)
        logins.button().click()
        logins.userid().send_keys(logins.user_name())
        logins.passwrod().send_keys(logins.password_name())
        logins.button_01().click()
        time.sleep(60)
    except Exception as e:
        raise e
