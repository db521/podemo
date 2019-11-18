from pageobject.loginpage import login
import time
def loginS(driver,name,passwd):
    try:
        logins = login(driver)
        time.sleep(2)
        logins.zhangHkuang().send_keys(name)
        logins.miMkuang().send_keys(passwd)
        logins.dengLanniu().click()
        time.sleep(3)
    except Exception as e:
        raise e

if __name__ == '__main__':
    pass