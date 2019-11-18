from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


def get_elementObj(driver,locate,locateExpression):

    elementObj = WebDriverWait(driver,30,0.5).until(lambda x:x.find_element(by=locate,value=locateExpression))
    return elementObj

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://127.0.0.1:81/biz/user-login-L2Jpei8=.html')
    print(get_elementObj(driver,"id","submit"))