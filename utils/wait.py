from selenium.webdriver.support.ui import WebDriverWait
def XianShiAndFind(driver,fangFa,biaoDaShi):
    try:
        element = WebDriverWait(driver,10,0.2).until(lambda x:x.find_element(by=fangFa,value=biaoDaShi))
        return element
    except Exception as e:
        print(e)