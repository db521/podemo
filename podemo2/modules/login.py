from pageobject.pageobjects import access


def LoginSup(driver):
    try:
        assecct = access(driver)

        assecct.userObj().send_keys(assecct.userREd())
        assecct.pwdObj().send_keys(assecct.pwdREd())
        assecct.btnObj().click()
    except Exception as e:
        raise e
