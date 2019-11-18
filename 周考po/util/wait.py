from selenium.webdriver.support.ui import WebDriverWait

def getelement(dr,type,grammar):
    try:
        element = WebDriverWait(dr,10).until(lambda x:x.find_element(by=type,value=grammar))
        return element

    except Exception as e:
        raise 