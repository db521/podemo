# -*- coding: utf-8 -*-
# import vie,ser,oth,mod,url
from selenium.webdriver.support.ui import WebDriverWait
def getElementImplicitWait(driver,locatetype,locatorExpection):
    """
    传入一个定位的元素，然后自动进行显式等待
    :return:
    """
    try:
        element=WebDriverWait(driver,30).until(lambda x:x.find_element(by=locatetype,value=locatorExpection))
        return element
    except Exception as e:
        raise e
    pass
