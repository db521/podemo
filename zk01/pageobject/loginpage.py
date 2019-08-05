from ..util.wait import getele as ge
import json
from selenium import webdriver
class login:
    def __init__(self,driver):
        self.driver = driver
    def xixi(self):
        try:
            with open('D:\pythontest\zk01\config\aa.json','r',encoding='utf-8')as f:
                ss = json.loads(f.read())
            sa = ss["login"]["ztbt"]
            loaa = sa[0]
            lobb = sa[1]
            asa = ge(self.driver,loaa,lobb)
            return asa
        except Exception as r:
            raise r
    def  zhang(self):
        try:
            with open('D:\pythontest\zk01\config\aa.json','r',encoding='utf-8') as f:
                ss = json.loads(f.read())
            sa = ss["login"]["name"]
            loaa = sa[0]
            lobb = sa[1]
            asa = ge(self.driver, loaa, lobb)
            return asa
        except Exception as e:
            raise e
    def  name(self):
        try:
            with open('D:\pythontest\zk01\config\aa.json','r',encoding='utf-8') as f:
                ss = json.loads(f.read())
            sa = ss["user"]
            return sa
        except Exception as e:
            raise e
    def  miding(self):
        try:
            with open('D:\pythontest\zk01\config\aa.json','r',encoding='utf-8') as f:
                ss = json.loads(f.read())
            sa = ss["login"]["passwd"]
            loaa = sa[0]
            lobb = sa[1]
            asa = ge(self.driver, loaa, lobb)
            return asa
        except Exception as e:
            raise e
    def  psswd(self):
        try:
            with open('D:\pythontest\zk01\config\aa.json','r',encoding='utf-8') as f:
                ss = json.loads(f.read())
            sa = ss["passwd"]
            return sa
        except Exception as e:
            raise e
    def  obje(self):
        try:
            with open('D:\pythontest\zk01\config\aa.json','r',encoding='utf-8') as f:
                ss=json.loads(f.read())
            aa = ss['login']['btn']
            ab=aa[0]
            bb=aa[1]
            agee = ge(self.driver,ab,bb)
            return agee
        except Exception as e:
            raise e
    def fengz(self):
        with open('D:\pythontest\zk01\config\aa.json', 'r', encoding='utf-8') as f:
            sw = json.loads(f.read())
            try:
                dict = sw['login']
                for key in dict.keys():
                    ss = sw["login"]["{}".format(key)]
                    locatetype = ss[0]
                    locatorExpression = ss[1]
                    print(key)
                    print(locatetype, locatorExpression)
                    elemetObj = ge(self.driver, locatetype, locatorExpression)
            except Exception as e:
                raise e
if __name__ == '__main__':
        driver = webdriver.Chrome()
        logins = login(driver)
        logins.fengz()