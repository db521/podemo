from util.wait import getWait as ge
import json

class login:
    def __init__(self,driver):
        self.driver=driver

    def nameObj(self):
        try:
            with open('../config/pageobject.json','r',encoding='utf-8') as f:
                sw=json.loads(f.read())
            ss=sw["login"]["name"]
            locatetype=ss[0]
            locatorExpression=ss[1]
            elementObj=ge(self.driver,locatetype,locatorExpression)
            return elementObj

        except Exception as e:
            raise e

    def passwdObj(self):
        try:
            with open('../config/pageobject.json','r',encoding='utf-8') as f:
                sw=json.loads(f.read())
            ss=sw["login"]["passwd"]
            locatetype=ss[0]
            locatorExpression=ss[1]
            elementObj=ge(self.driver,locatetype,locatorExpression)
            return elementObj

        except Exception as e:
            raise e

    def btnObj(self):
        try:
            with open('../config/pageobject.json','r',encoding='utf-8') as f:
                sw=json.loads(f.read())
            ss=sw["login"]["btn"]
            locatetype=ss[0]
            locatorExpression=ss[1]
            elementObj=ge(self.driver,locatetype,locatorExpression)
            return elementObj

        except Exception as e:
            raise e