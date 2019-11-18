from pageobject.login import login as lo
import time


def login(dr,username,password):
    try:
        logins = lo(dr)
        logins.name().send_keys(username)
        logins.password().send_keys(password)
        logins.button().click()
        time.sleep(2)
    except Exception as e:
        raise e