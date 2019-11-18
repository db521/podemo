from selenium.webdriver.support.ui import WebDriverWait

def getWebDriver(driver,locatetype,locatevalue):
    """
    显示等待，30s内，每0.5秒轮询一次
    :param driver:
    :param locatetype:
    :param locatevalue:
    :return:

    """
    try:
        return WebDriverWait(driver,30,0.5).until(lambda x:x.find_element(by=locatetype,value=locatevalue))
    except Exception as e:
        raise e
