from pageobject.loginpage import Login

def LoginStep(driver,user,passwd):
    """
    具体去做登陆操作
    :param driver:
    :param user:
    :param passwd:
    :return:
    """
    try:
        login = Login(driver)
        login.UserObj().send_keys(user)
        login.Passwordobj().send_keys(passwd)
        login.Loginobj().click()

    except Exception as e:
        raise e
