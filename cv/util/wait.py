



from selenium.webdriver.support.wait import WebDriverWait



def getl(driver,id,vee):
    try:
        element = WebDriverWait(driver,40).until(lambda x:x.find_element(by=id,value=vee))
        return element

    except Exception as e:
        raise e


