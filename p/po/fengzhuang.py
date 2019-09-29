import json
from util.dengdai import getElementImplicitWait as ge
from selenium import webdriver
class Login():
    def __init__(self,driver):
        self.driver=driver
    def name(self):
        try:
            with open('D:\Django\untitled\p\cofig\dingwei.json','r')as f:
                duqu=json.loads(f.read())
                key=duqu["login"]["name"]
                zhi=key[0]
                zhi1=key[1]
                yuansu=ge(self.driver,zhi,zhi1)
                return yuansu

        except Exception as e:
            print(e)
    def passwd(self):
        try:
            with open('D:\Django\untitled\p\cofig\dingwei.json',"r",encoding="utf-8")as f:
                    duqu=json.loads(f.read())
                    key=duqu["login"]["passwd"]
                    zhi=key[0]
                    zhi1=key[1]
                    yuansu=ge(self.driver,zhi,zhi1)
                    return yuansu
        except Exception as e:
            print(e)
    def btn(self):
        try:
            with open('D:\Django\untitled\p\cofig\dingwei.json')as f:
                duqu=json.loads(f.read())
                key=duqu["login"]["btn"]
                zhi=key[0]
                zhi1=key[1]
                yuansu=ge(self.driver,zhi,zhi1)
                return yuansu

        except Exception as e:
            print(e)
if __name__ == '__main__':
    driver=webdriver.Chrome()
    logins=Login(driver)
    logins.name()
