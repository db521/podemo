from pageobject.loginPage import login
from selenium.webdriver.common.keys import Keys

def Addbumen(driver,ejk):
    try:
        logins = login(driver)
        logins.zuzhiObj().click()
        logins.addObj().click()
        logins.ejbumen().click()
        logins.Shuru().send_keys(ejk+Keys.ENTER)



        # 登陆操作
    except Exception as e:
        raise e

if __name__ == '__main__':
    pass