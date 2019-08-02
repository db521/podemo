import json
from util.wait import getElementWait as ge
from selenium import webdriver

class Login:

    def __init__(self,driver):
        self.driver = driver

    def buttonUser(self):
        try:
            with open('D:\PO\zentao\config\pageobject.json','r',encoding='utf-8') as f:
                btn = json.loads(f.read())
                but = btn["login"]["name"]
                result = but[1]
                locatetype = but[0]
                print(result)
                elementobj = ge(self.driver,locatetype,result)
                return elementobj
        except Exception as e:
            raise e


if __name__ == '__main__':
    driver = webdriver.Chrome()
    logins = Login(driver)



