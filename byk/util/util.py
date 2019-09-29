# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
def getElementImplicitwait(driver,locatetype,locatorExpection):
    try:
        element=WebDriverWait(driver,30).until(lambda x:x.find_element(by=locatetype,value=locatorExpection))
        return element
    except Exception as e:
        pass
