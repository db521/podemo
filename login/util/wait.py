from selenium.webdriver.support.ui import WebDriverWait

def getport(driver,assd,bssd):
    try:
        element = WebDriverWait(driver,30,0.5).until(lambda x:x.find_element(by=assd,value=bssd))
        return element
    except Exception as e:
        raise e