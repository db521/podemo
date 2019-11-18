
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

def getElementImplicitWait(driver,locatetype,locatorExpection):
    """
    传入一个定位的元素，然后自动进等待
    :return:
    lambda x:xx
    """
    try:
        print(type(locatetype))
        element=WebDriverWait(driver,30).until(lambda x:x.find_element(eval(locatetype),locatorExpection))
        return element
    except Exception as e:
        raise e

