import json
from selenium import webdriver
from util.wait import getElement as wait

class  Login:
    def __init__(self,driver):
        self.driver = driver

    def ver(self):
        try:
            with open("D:\Python\Django\lianxi\config\pageobject.json","r+") as f:
                js = json.loads(f.read())
                btn = js["login"]['zentao']
                btntype = btn[0]
                btnobj = btn[1]
                verobj = (btntype,btnobj)
                print(verobj)
                return wait(self.driver,btntype,btnobj)

        except Exception as e:
            raise e
    def userread(self):
        try:
            with open(r"D:\Python\Django\lianxi\config\user.json","r+",encoding='utf8') as f:
                    js = json.loads(f.read())
            user = js['user']

            print(user)
            return user
        except Exception as e:
            raise e

    def passwdread(self):
        try:
            with open(r"D:\Python\Django\lianxi\config\user.json", "r+", encoding='utf8') as f:
                js = json.loads(f.read())
            passwd = js['passwd']

            print(passwd)
            return passwd
        except Exception as e:
            raise e

    def useript(self):
        try:
            with open(r"D:\Python\Django\lianxi\config\pageobject.json", "r+",encoding='utf8') as f:
                js = json.loads(f.read())
            user = js['login']['user']
            usertype = user[0]
            userobj = user[1]
            print(user)
            return wait(self.driver,usertype,userobj)
        except Exception as e:
            raise e

    def passwdipt(self):
        try:

            with open(r"D:\Python\Django\lianxi\config\pageobject.json", "r+", encoding='utf8') as f:
                js = json.loads(f.read())
            passwd = js['login']['passwd']
            passwdtype = passwd[0]
            passwdobj = passwd[1]
            print(passwd)
            return wait(self.driver, passwdtype, passwdobj)

        except Exception as e:
            raise e

    def logbtn(self):
        try:

            with open(r"D:\Python\Django\lianxi\config\pageobject.json", "r+", encoding='utf8') as f:
                js = json.loads(f.read())
            logbtn = js['login']['btn']
            logtype = logbtn[0]
            logobj = logbtn[1]
            print(logbtn)
            return wait(self.driver, logtype, logobj)

        except Exception as e:
            raise e
