from selenium.webdriver.support.ui import WebDriverWait
def getele(driver,aa,bb):
    try:
        element = WebDriverWait(driver,30).until(lambda x:x.find_element(by=aa,value=bb))
        return  element
    except Exception as e:
        raise e
    pass
