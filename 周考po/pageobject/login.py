import json
from util.wait import getelement
class login:
    def __init__(self,dr):
        self.dr = dr
        with open('../config/pageobject.json','r',encoding='utf-8')as f:
            self.loginlist = json.loads(f.read())

    def name(self):
        try:
            v = self.loginlist["username"]
            type = v[0]
            value = v[1]
            element = getelement(self.dr,type,value)
            return element
        except Exception as e:
            raise e

    def password(self):
        try:
            v = self.loginlist["password"]
            type = v[0]
            value = v[1]
            element = getelement(self.dr,type,value)
            return element
        except Exception as e:
            raise e

    def button(self):
        try:
            v = self.loginlist["button"]
            type = v[0]
            value = v[1]
            element = getelement(self.dr,type,value)
            return element
        except Exception as e:
            raise e