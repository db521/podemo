from pageobject.loginpage import login
import time


def loginStep(driver, name, passwd):

    try:
        logins = login(driver)
        time.sleep(5)
        # 输入用户名
        logins.nameObj().send_keys(name)
        time.sleep(5)
        # 输入密码
        logins.passwdObj().send_keys(passwd)
        time.sleep(5)
        # 点击登陆按钮
        logins.buttonObj().click()

        time.sleep(5)  # 登陆之后等待5秒关闭

    except Exception as e:
        raise e