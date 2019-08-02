#coding=utf-8;
from selenium.webdriver.support.ui import WebDriverWait
def getElementImplicitWait(driver,locatetype,locatorExpection):
    element=WebDriverWait(driver,30).until(lambda x:x.find_element(by=locatetype,value=locatorExpection))
    return element