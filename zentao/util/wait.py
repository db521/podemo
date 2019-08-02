from selenium.webdriver.support.ui import WebDriverWait


def getElementWait(driver, locatetype, locateExpression):
    """
    传入一个定位元素,然后进行隐式等待
    :param driver:
    :param locatetype:
    :param locateException:
    :return:
    """
    try:
        element = WebDriverWait(driver, 30).until(lambda x: x.find_element(by=locatetype, value=locateExpression))
        return element
    except Exception as e:
        raise e
    pass
