from selenium.webdriver.support.wait import WebDriverWait

def getWait(driver,locatetype,locatorExpression):
    try:
        element=WebDriverWait(driver,30).until(lambda x:x.find_element(by=locatetype,value=locatorExpression))
        return element

    except Exception as e:
        raise e
