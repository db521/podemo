from ..pageobject.loginpage import login
def loginstep(drive):
    try:
        logins = login(drive)
        logins.xixi().click()
        logins.zhang().send_keys(logins.name())
        logins.miding().send_keys(logins.psswd())
        logins.obje().click()
    except Exception as e:
        raise e






