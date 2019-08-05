from pageobject.login import login

def logStep(driver):
    try:

        logs = login(driver)

        logs.zentao().click()
        logs.userinput().send_keys(logs.userread())
        logs.passwdinput().send_keys(logs.passwdread())
        logs.loginbtn().click()
        logs.zuzhi().click()
        logs.bumen().click()
        logs.add().click()
        logs.addbumen().senk_keys('asdas')

    except Exception as e:
        raise e
