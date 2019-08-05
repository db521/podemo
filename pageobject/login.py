from selenium import webdriver
import json
from utils.wait import getwait as gw
class login:
    def __init__(self,driver):
        self.driver = driver

    def zentao(self):
        try:
            with open(r'D:\Python\Django\week1\config\pageobject.json',"r+",encoding="utf8") as f:
                js = json.loads(f.read())
                zenbtn = js['login']['zentao']
                zentype = zenbtn[0]
                zenexe = zenbtn[1]
                print(zenbtn)
                return gw(self.driver,zentype,zenexe)

        except Exception as e:
            raise e


    def userread(self):
        try:
            with open(r'D:\Python\Django\week1\config\user.json',"r+",encoding="utf8") as f:
                js = json.loads(f.read())
                user = js['user']
                print(user)
                return user

        except Exception as e:
            raise e

    def passwdread(self):
        try:
            with open(r'D:\Python\Django\week1\config\user.json',"r+",encoding="utf8") as f:
                js = json.loads(f.read())
                passwd = js['passwd']

                print(passwd)
                return passwd

        except Exception as e:
            raise e

    def userinput(self):
        try:
            with open(r'D:\Python\Django\week1\config\pageobject.json',"r+",encoding="utf8") as f:
                js = json.loads(f.read())
                userinput = js['login']['user']
                userinputtype = userinput[0]
                userinputexe = userinput[1]
                print(userinput)
                return gw(self.driver,userinputtype,userinputexe)

        except Exception as e:
            raise e

    def passwdinput(self):
        try:
            with open(r'D:\Python\Django\week1\config\pageobject.json',"r+",encoding="utf8") as f:
                js = json.loads(f.read())
                passwdinput = js['login']['passwd']
                passwdinputtype = passwdinput[0]
                passwdinputexe = passwdinput[1]
                print(passwdinput)
                return gw(self.driver,passwdinputtype,passwdinputexe)

        except Exception as e:
            raise e


    def loginbtn(self):
        try:
            with open(r'D:\Python\Django\week1\config\pageobject.json',"r+",encoding="utf8") as f:
                js = json.loads(f.read())
                loginbtn = js['login']['btn']
                loginbtntype = loginbtn[0]
                loginbtnexe = loginbtn[1]
                print(loginbtn)
                return gw(self.driver,loginbtntype,loginbtnexe)

        except Exception as e:
            raise e

    def zuzhi(self):
        try:
            with open(r'D:\Python\Django\week1\config\pageobject.json',"r+",encoding="utf8") as f:
                js = json.loads(f.read())
                zuzhi = js['login']['zuzhi']
                zuzhitype = zuzhi[0]
                zuzhiexe = zuzhi[1]
                print(zuzhi)
                return gw(self.driver,zuzhitype,zuzhiexe)

        except Exception as e:
            raise e

    def bumen(self):
        try:
            with open(r'D:\Python\Django\week1\config\pageobject.json',"r+",encoding="utf8") as f:
                js = json.loads(f.read())
                bumen = js['login']['bumen']
                bumentype = bumen[0]
                bumenexe = bumen[1]
                print(bumen)
                return gw(self.driver,bumentype,bumenexe)

        except Exception as e:
            raise e

    def add(self):
        try:
            with open(r'D:\Python\Django\week1\config\pageobject.json',"r+",encoding="utf8") as f:
                js = json.loads(f.read())
                add = js['login']['add']
                addtype = add[0]
                addexe = add[1]
                print(add)
                return gw(self.driver,addtype,addexe)

        except Exception as e:
            raise e

    def addbumen(self):
        try:
            with open(r'D:\Python\Django\week1\config\pageobject.json',"r+",encoding="utf8") as f:
                js = json.loads(f.read())
                addname = js['login']['addname']
                addnametype = addname[0]
                addnameexe = addname[1]
                print(addname)
                return gw(self.driver,addnametype,addnameexe)

        except Exception as e:
            raise e



if __name__ == "__main__":
    driver  = webdriver.Chrome()
    logi = login(driver)
    logi.zentao()
