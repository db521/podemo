import json
from selenium.webdriver.support.ui import WebDriverWait

def getWait(driver,shu1,shu2):
    try:
        element = WebDriverWait(driver,20).until(lambda x:x.find_element(by=shu1,value=shu2))
        return element
    except Exception as e:
        raise e