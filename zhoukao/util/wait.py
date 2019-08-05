from selenium.webdriver.support.wait import WebDriverWait


def getElementWait(driver,locatetype,locateExpression):

    """
    传入一个元素，进入隐式等待
    :param driver:
    :param locatetype:
    :param locateExpression:
    :return:
    """

    try:
        element = WebDriverWait(driver,30).until(lambda x:x.find_element(by=locatetype,value=locateExpression))
        return element

    except Exception as e:
        raise e