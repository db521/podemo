from selenium.webdriver.support.ui import WebDriverWait


def Webdriverait(driver, exceptype, exception):
    try:
        element = WebDriverWait(driver, 30).until(lambda x: x.find_element(by=exceptype, value=exception))
        return element
    except Exception as e:
        raise e
    pass
