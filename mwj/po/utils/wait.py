from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains

def getWait(driver,typ,lj):
    try:
        elment = WebDriverWait(driver,30,0.5).until(lambda x:x.find_element(by=typ,value=lj))
        return elment

    except Exception as e:
        raise e

def gait(driver, typ, lj):
    try:
        element = ActionChains(driver).move_to_element(driver.find_element(by=typ,value=lj)).perform()

        return element
    except Exception as e:
        raise e