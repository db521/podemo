from selenium.webdriver.support.wait import WebDriverWait

def getWat(driver,locatype,locatEception):
    try:
        element = WebDriverWait(driver,20,0.5).until(lambda x:x.find_element(by=locatype,value=locatEception))
        return element
    except Exception as e:
        raise e