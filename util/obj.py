from util.wait import getElementImplicitWait as ge
from selenium.webdriver.common.by import By
def obj(driver,sw,key1,key2):
    try:
        ss = sw[key1][key2]
        locatetype = ss[0]
        locatorExpression = ss[1]
        elemetObj = ge(driver, locatetype, locatorExpression)
        return elemetObj
    except Exception as e:
        raise e