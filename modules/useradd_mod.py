# 添加用户元素操作
from pageobjects.useradd import Useradd
from utils.read_json import read_user as ru
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def Useradd_Mod(driver):
    # 获取元素
    us = Useradd(driver)
    # 进入添加用户页面
    us.zuzhi().click()
    us.useradd().click()
    # 填入信息
    us.username().send_keys(ru('username'))
    us.password().send_keys(ru('password'))
    us.password2().send_keys(ru('password2'))
    us.name().send_keys(ru('name'))
    sel = us.zhiwei()
    Select(sel).select_by_visible_text(ru('zhiwei'))
    sel2 = us.group()
    Select(sel2).select_by_visible_text(ru('group'))
    us.yuser().send_keys(ru('yuser'))
    us.ypasswd().send_keys(ru('ypasswd'))
    # 点击保存按钮
    element = us.sver()
    driver.execute_script("arguments[0].click();", element)
    # 显式等待
    WebDriverWait(driver,10,0.2).until(ec.element_to_be_clickable)



