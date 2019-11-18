import time,json

from untils.wait import getWat as ge

class Login():
    def __init__(self,driver):
        self.driver = driver
        self.driver.maximize_window()
    def nameobj(self):
        try:
            with open('../config/page.json','r') as f:
                nn = json.loads(f.read())
            su = nn["login"]["name"]
            locatype = su[0]
            locatEception = su[1]
            element = ge(self.driver,locatype,locatEception)
            return element
        except Exception as e:
            raise e

    def passwdobj(self):
        try:
            with open('../config/page.json','r') as f:
                nn = json.loads(f.read())
            su = nn["login"]["passwd"]
            locatype = su[0]
            locatEception = su[1]
            element = ge(self.driver,locatype,locatEception)
            return element
        except Exception as e:
            raise e

    def buttenobj(self):
        try:
            with open('../config/page.json','r') as f:
                nn = json.loads(f.read())
            su = nn["login"]["butten"]
            locatype = su[0]
            locatEception = su[1]
            element = ge(self.driver,locatype,locatEception)
            return element
        except Exception as e:
            raise e