from selenium.webdriver.support.ui import WebDriverWait

def getElementImplicitWait(driver, type, locatorExpection):

    try:
        element = WebDriverWait(driver,30).until(lambda x:x.find_element(by=type, value=locatorExpection))
        return element
    except Exception as e:
        raise e
    pass


