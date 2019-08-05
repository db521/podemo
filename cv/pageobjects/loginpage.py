



import json

from selenium import webdriver
from util.wait import getl
class login():
    def __init__(self,driver):
        self.driver = driver

    def kaiyuan(self):
        with open('../config/element.json','r')as f:
            ment = json.loads(f.read())

            idd= ment["login"]["ztbt"]
            ipd = idd[0]
            iid = idd[1]
            su = getl(self.driver,ipd,iid)
            return su

    def userr(self):
        with open('../config/element.json','r')as f:
            ment = json.loads(f.read())

            idd= ment["login"]["userr"]

            ipd = idd[0]
            iid = idd[1]
            su = getl(self.driver, ipd, iid)
            return su

    def userinput(self):
        with open('../config/element.json', 'r')as f:
            ment = json.loads(f.read())

            idd = ment["login"]["input1"]


            return idd

    def passwd(self):
        with open('../config/element.json','r')as f:
            ment = json.loads(f.read())

            idd= ment["login"]["passwd"]

            ipd = idd[0]
            iid = idd[1]
            su = getl(self.driver, ipd, iid)
            return su

    def passwordinput(self):
        with open('../config/element.json', 'r')as f:
            ment = json.loads(f.read())

            idd = ment["login"]["password"]


            return idd


    def loginclick(self):
        with open('../config/element.json', 'r')as f:
            ment = json.loads(f.read())

            idd = ment["login"]["loginclick"]

            ipd = idd[0]
            iid = idd[1]
            su = getl(self.driver, ipd, iid)
            return su

    def zu(self):
        with open('../config/element.json', 'r')as f:
            ment = json.loads(f.read())

            idd = ment["login"]["zuzhi"]

            ipd = idd[0]
            iid = idd[1]
            su = getl(self.driver, ipd, iid)
            return su

    def bu(self):
        with open('../config/element.json', 'r')as f:
            ment = json.loads(f.read())

            idd = ment["login"]["bumen"]

            ipd = idd[0]
            iid = idd[1]
            su = getl(self.driver, ipd, iid)
            return su
    def song(self):
        with open('../config/element.json', 'r')as f:
            ment = json.loads(f.read())

            idd = ment["login"]["song"]

            ipd = idd[0]
            iid = idd[1]
            su = getl(self.driver, ipd, iid)
            return su
    def zeng(self):
        with open('../config/element.json', 'r')as f:
            ment = json.loads(f.read())

            idd = ment["login"]["zeng"]

            ipd = idd[0]
            iid = idd[1]
            su = getl(self.driver, ipd, iid)
            return su
    def bumeninput(self):
        with open('../config/element.json', 'r')as f:
            ment = json.loads(f.read())

            idd = ment["login"]["zengiput"]


            return idd

    def busmb(self):
        with open('../config/element.json', 'r')as f:
            ment = json.loads(f.read())

            idd = ment["login"]["busum"]

            ipd = idd[0]
            iid = idd[1]
            su = getl(self.driver, ipd, iid)
            return su


