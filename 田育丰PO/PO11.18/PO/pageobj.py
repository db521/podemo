from until.wait import getElment as g
import json
from selenium import webdriver

class login:
    def __init__(self,driver):
        self.driver=driver

    def urlobj(self):
        try:
            with open('../config/wz.json','r') as f:
                url=json.loads(f.read())
                return url
        except Exception as e:
            raise e
    def nameobj(self):
        try:
            with open('../config/login.json','r') as f:
                e=json.loads(f.read())
                a=e["login"]["name"]
                types=a[0]
                velue=a[1]
                element=g(self.driver,types,velue)
            return element
        except Exception as e:
            raise e
    def passwdobj(self):
        try:
            with open('../config/login.json','r') as f:
                e=json.loads(f.read())
                a=e["login"]["passwd"]
                types=a[0]
                velue=a[1]
                element=g(self.driver,types,velue)
                return element
        except Exception as e:
            raise e

    def submitobj(self):
        try:
            with open('../config/login.json','r') as f:
                e=json.loads(f.read())
                a=e["login"]["submit"]
                types=a[0]
                velue=a[1]
                element=g(self.driver,types,velue)
                return element
        except Exception as e:
            raise e
# if __name__ == '__main__':
#     driver=webdriver.Chrome()
#     log=login(driver)
#     log.urlobj()
#     log.passwdobj()
#     log.submitobj()

