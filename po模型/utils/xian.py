from selenium.webdriver.support.ui import WebDriverWait

def getxian(driver,key,value):
    try:
        e=WebDriverWait(driver,30).until(lambda x:x.find_element(by=key,value=value))
        return e
    except EnvironmentError as e:
        raise e