from selenium.webdriver.support.ui import WebDriverWait

def getWebDriverWait(driver,locatetype,locatevalue):

    try:
        return WebDriverWait(driver,30,0.5).until(lambda x:x.find_element(by=locatetype,value=locatevalue))
    except Exception as e:
        raise e






