# 登录页元素操作
from pageobjects.loginPage import Login_page
from utils.read_json import read_user as ru
def LoginMod(driver):
    # 获取元素
    login = Login_page(driver)
    # 输入框填入数据 点击登录按钮
    login.usename().send_keys(ru('yuser'))
    login.passwd().send_keys(ru('ypasswd'))
    login.button().click()


