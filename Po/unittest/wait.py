from selenium.webdriver.support.ui import WebDriverWait


def getElement(driver, locatetype, locatorExpression):

    try:
        element = WebDriverWait(driver, 30, 0.5)\
            .until(lambda x: x.find_element(by=locatetype, value=locatorExpression))
        return element
    except Exception as f:
        raise f