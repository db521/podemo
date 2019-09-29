# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait


def getElementImplicitWait(driver,locatetype,locatorExpection):
    """

    :param driver:
    :param locatetype:
    :param locatorExpection:
    :return:
    """
    try:
        element=WebDriverWait(driver,30).until(lambda x:x.find_element(by=locatetype,value=locatorExpection))
        return element
    except Exception as e:
        raise e
    pass