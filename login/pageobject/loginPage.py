from util.wait import getport as ge
import json


class login:
    def __init__(self,driver):
        self.driver=driver

    def nameObj(self):
        try:
            with open('../config/pageobject.json','r',encoding='utf-8') as f:
                sw = json.loads(f.read())
            ss = sw["login"]["name"]
            assd = ss[0]
            bssd = ss[1]
            ejmobj = ge(self.driver,assd,bssd)
            return ejmobj
        except Exception as e:
            raise e

    def passwordObj(self):
        try:
            with open('../config/pageobject.json','r',encoding='utf-8') as f:
                sw = json.loads(f.read())
            ss = sw["login"]["password"]
            assd = ss[0]
            bssd = ss[1]
            ejmobj = ge(self.driver,assd,bssd)
            return ejmobj
        except Exception as e:
            raise e

    def btnObj(self):
        try:
            with open('../config/pageobject.json','r',encoding='utf-8') as f:
                sw = json.loads(f.read())
            ss = sw["login"]["btn"]
            assd = ss[0]
            bssd = ss[1]
            ejmobj = ge(self.driver,assd,bssd)
            return ejmobj
        except Exception as e:
            raise e