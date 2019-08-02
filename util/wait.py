from selenium.webdriver.support.ui import WebDriverWait

def getElement(driver,locatetype,locaExpeciton):
    try:
       element = WebDriverWait(driver,30).until(lambda a:a.find_element(by=locatetype,value=locaExpeciton))

       return element

    except Exception as e:
        raise e

