from wg12b.util.parsejson import parselocator as pl
from wg12b.util.parsejson import parseurl as purl
from wg12b.util.parsejson import parseuser as puser
from wg12b.util.wait import getElementImplicitWait as ge
from selenium.webdriver.common.keys import Keys


class Login():
    def __init__(self,driver):
        self.driver = driver

    def deng(self):
        try:
            url = purl('url')
            self.driver.get(url)
        except Exception as e:
            raise e

    def zentao(self):
        try:
            zentao = pl("login", "zentao")
            property = zentao[0]
            location = zentao[1]
            loginbtn = ge(self.driver,property,location)
            loginbtn.click()
            return loginbtn
        except Exception as e:
            raise e

    def name(self):
        try:
            name = pl("login", "name")
            property = name[0]
            location = name[1]
            elem = ge(self.driver, property, location)
            users = puser("name")
            elem.send_keys(users)
            return elem
        except Exception as e:
            raise e

    def passwd(self):
        try:
            passwd = pl("login", "passwd")
            property = passwd[0]
            location = passwd[1]
            elem = ge(self.driver, property, location)
            users = puser("passwd")
            elem.send_keys(users + Keys.ENTER)
            return elem
        except Exception as e:
            raise e



if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    login = Login(driver)
    login.deng()
    login.zentao()
    login.name()
    login.passwd()

















