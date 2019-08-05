from selenium.webdriver.support.ui import WebDriverWait

def getwait(driver,locatetype,locatExepetion):

    try:
        element = WebDriverWait(driver,30).until(lambda a:a.find_element(by=locatetype,value=locatExepetion))
        return element
    except Exception as e:
        raise e