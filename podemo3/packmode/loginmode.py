import json
from selenium import webdriver
from util.wait import getElementImplicitWait as ge

class login():
    def __init__(self,web):
        self.web=web

    def nameobj(self):
        try:
            with open('../login/packlogin.json','r',encoding='utf8')as f:
                aa=json.loads(f.read())
            up=aa['login']['name']
            locatetype=up[0]
            locatorExpection=up[1]
            namesobj=ge(self.web,locatetype,locatorExpection)
            return namesobj
        except Exception as e:
            raise e

    def passwdobj(self):
        try:
            with open('../login/packlogin.json','r',encoding='utf8')as f:
                aa=json.loads(f.read())
            up=aa['login']['passwd']
            locatetype=up[0]
            locatorExpection=up[1]
            passwdsobj=ge(self.web,locatetype,locatorExpection)
            return passwdsobj
        except Exception as e:
            raise e

    def clickobj(self):
        try:
            with open('../login/packlogin.json','r',encoding='utf8')as f:
                aa=json.loads(f.read())
            up=aa['login']['click']
            locatetype=up[0]
            locatorExpection=up[1]
            clicksobj=ge(self.web,locatetype,locatorExpection)
            return clicksobj
        except Exception as e:
            raise e


if __name__ == '__main__':
    web=webdriver.Chrome()
    abc=login(web)
    abc.nameobj()

