from selenium.webdriver.support.ui import WebDriverWait

def getElment(driver,locateType,locateException):
    try:
        element=WebDriverWait(driver,30).until(lambda x:x.find_element(by=locateType,value=locateException))
        return element
    except Exception as e:
        raise e
    pass