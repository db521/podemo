from selenium import webdriver
from config import *
from utils.xian import getxian as ge
import json
class login:
    def __init__(self,driver):
        self.driver=driver

    def button(self):
        try:
            with open("../config/login.json","r",encoding="utf-8") as f:
                ss=json.loads(f.read())
            but=ss["login"]["button"]
            key=but[0]
            value=but[1]
            but_click=ge(self.driver,key,value)
            print(but)
            return but_click
        except:
            raise

    def userid(self):
        try:
            with open("../config/login.json", "r", encoding="utf-8") as f:
                ss = json.loads(f.read())
            but = ss["login"]["username"]
            key = but[0]
            value = but[1]
            user_id = ge(self.driver, key, value)
            print(but)
            return user_id
        except:
            raise

    def user_name(self):
        try:
            with open("../config/user.json", "r", encoding="utf-8") as f:
                ss = json.loads(f.read())
            but = ss["username"]
            print(but)
            return but
        except:
            raise

    def passwrod(self):
        try:
            with open("../config/login.json", "r+", encoding="utf-8") as f:
                ss = json.loads(f.read())
            but = ss["login"]["password"]
            key = but[0]
            value = but[1]
            passwrod_id = ge(self.driver, key, value)
            print(but)
            return passwrod_id
        except:
            raise

    def  password_name(self):
        try:
            with open("../config/user.json", "r", encoding="utf-8") as f:
                ss = json.loads(f.read())
            but = ss["password"]
            print(but)
            return but
        except:
            raise

    def button_01(self):
        try:
            with open("../config/login.json","r+",encoding="utf-8") as f:
                ss=json.loads(f.read())
            but=ss["login"]["button_01"]
            key=but[0]
            value=but[1]
            but_click=ge(self.driver,key,value)
            return but_click
        except EnvironmentError as e:
            raise e


