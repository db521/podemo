from selenium.webdriver.support.ui import WebDriverWait

def getElementWebDriverWait(driver,locatuType,locatorElement):
    try:

        element=WebDriverWait(driver,100).until(lambda x:x.find_element(by=locatuType,value=locatorElement))
        return element

    except Exception as e:
        raise e