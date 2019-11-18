from selenium.webdriver.support.ui import WebDriverWait

def getWebDriverWait(driver,locatype,locavalue):
    try:
        element = WebDriverWait(driver,10,0.5).until(lambda x:x.find_element(by=locatype,value=locavalue))
        return element
    except Exception as e:
        raise e