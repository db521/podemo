#coding=utf-8;
import json
from util.wait import getElementImplicitWait as ge
from selenium import webdriver
class login:
    def __init__(self,driver):
        self.driver=driver
    def zdbtn_click(self):
        with open(r"F:\Ce-shi\chandao_po\config\pageproject.json",'r',encoding='utf-8')as f:
            pageproject=json.loads(f.read())
            pageobj_value=pageproject['login']['zdbtn']
            zd_id=pageobj_value[0]
            zd_value=pageobj_value[1]
            elementobj=ge(self.driver,zd_id,zd_value)
            return elementobj
    def root_id_inut(self):
        with open(r"F:\Ce-shi\chandao_po\config\pageproject.json", 'r', encoding='utf-8')as f:
            pageproject=json.loads(f.read())
            pageobj_value=pageproject['login']['name']
            zd_id=pageobj_value[0]
            zd_value=pageobj_value[1]
            elementobj = ge(self.driver, zd_id,zd_value)
            return elementobj
    def root_pwd_inut(self):
        with open(r"F:\Ce-shi\chandao_po\config\pageproject.json", 'r', encoding='utf-8')as f:
            pageproject = json.loads(f.read())
            pageobj_value = pageproject['login']['passwd']
            zd_id = pageobj_value[0]
            zd_value = pageobj_value[1]
            elementobj = ge(self.driver, zd_id, zd_value)
            return elementobj
    def denglu_click(self):
        with open(r"F:\Ce-shi\chandao_po\config\pageproject.json",'r',encoding='utf-8')as f:
            pageproject=json.loads(f.read())
            pageobj_value=pageproject['login']['btn']
            zd_id=pageobj_value[0]
            zd_value=pageobj_value[1]
            elementobj=ge(self.driver,zd_id,zd_value)
            return elementobj
    def zuzhi_click(self):
        with open(r"F:\Ce-shi\chandao_po\config\pageproject.json",'r',encoding='utf-8')as f:
            pageproject=json.loads(f.read())
            pageobj_value=pageproject['login']['zuzhi']
            zd_id=pageobj_value[0]
            zd_value=pageobj_value[1]
            elementobj=ge(self.driver,zd_id,zd_value)
            return elementobj
    def bumen_click(self):
        with open(r"F:\Ce-shi\chandao_po\config\pageproject.json",'r',encoding='utf-8')as f:
            pageproject=json.loads(f.read())
            pageobj_value=pageproject['login']['bumen']
            zd_id=pageobj_value[0]
            zd_value=pageobj_value[1]
            elementobj=ge(self.driver,zd_id,zd_value)
            return elementobj

    def sty_click(self):
        with open(r"F:\Ce-shi\chandao_po\config\pageproject.json", 'r', encoding='utf-8')as f:
            pageproject = json.loads(f.read())
            pageobj_value = pageproject['login']['sty']
            zd_id = pageobj_value[0]
            zd_value = pageobj_value[1]
            elementobj = ge(self.driver, zd_id, zd_value)
            return elementobj


if __name__ == '__main__':
    driver=webdriver.Chrome()
    logins=login(driver)