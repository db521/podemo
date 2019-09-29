# -*- coding: utf-8 -*-
'''
@Time    : 2019/9/28 9:30
@Author  : Allen
@File    : .py
'''
from selenium.webdriver.support.ui import WebDriverWait
def website(driver,url):
    try:
        return driver.get(url)
    except Exception as e:
        raise e

def getElementImplicitWait(driver, locatetype, locatorExpection):
    """
    传入一个定位的元素，然后自动进行隐式等待
    :return:
    """

    try:
        element = WebDriverWait(driver, 30).until(lambda x: x.find_element(by=locatetype, value=locatorExpection))
        return element
    except Exception as e:
        raise e
    pass
