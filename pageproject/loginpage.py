# coding=utf-8;
import json
from util.wait import getElementImplicitWait as ge
from selenium import webdriver
class login:
    def __init__(self, driver):
        self.driver = driver
    def root_id_input(self):
        with open(r"F:\Ce-shi\zdl_po2019927\config\pageproject.json", 'r', encoding='utf-8')as f:
            pageproject = json.loads(f.read())
            pageobj_value = pageproject['login']['name']
            zd_id = pageobj_value[0]
            zd_value = pageobj_value[1]
            elementobj = ge(self.driver, zd_id, zd_value)
            return elementobj
    def root_pwd_input(self):
        with open(r"F:\Ce-shi\zdl_po2019927\config\pageproject.json", 'r', encoding='utf-8')as f:
            pageproject = json.loads(f.read())
            pageobj_value = pageproject['login']['passwd']
            zd_id = pageobj_value[0]
            zd_value = pageobj_value[1]
            elementobj = ge(self.driver, zd_id, zd_value)
            return elementobj
    def denglu_click(self):
        with open(r"F:\Ce-shi\zdl_po2019927\config\pageproject.json", 'r', encoding='utf-8')as f:
            pageproject = json.loads(f.read())
            pageobj_value = pageproject['login']['btn']
            zd_id = pageobj_value[0]
            zd_value = pageobj_value[1]
            elementobj = ge(self.driver,zd_id, zd_value)
            return elementobj
    def yonghu_click(self):
        with open(r"F:\Ce-shi\zdl_po2019927\config\pageproject.json", 'r', encoding='utf-8')as f:
            pageproject = json.loads(f.read())
            pageobj_value = pageproject['login']['yonghu']
            zd_id = pageobj_value[0]
            zd_value = pageobj_value[1]
            elementobj = ge(self.driver,zd_id, zd_value)
            return elementobj
    def useradd_click(self):
        with open(r"F:\Ce-shi\zdl_po2019927\config\pageproject.json", 'r', encoding='utf-8')as f:
            pageproject = json.loads(f.read())
            pageobj_value = pageproject['login']['useradd']
            zd_id = pageobj_value[0]
            zd_value = pageobj_value[1]
            elementobj = ge(self.driver,zd_id, zd_value)
            return elementobj
    def bumen_click(self):
        with open(r"F:\Ce-shi\zdl_po2019927\config\pageproject.json", 'r', encoding='utf-8')as f:
            pageproject = json.loads(f.read())
            pageobj_value = pageproject['login']['bumen']
            zd_id = pageobj_value[0]
            zd_value = pageobj_value[1]
            elementobj = ge(self.driver,zd_id, zd_value)
            return elementobj
    def zhiwei_click(self):
        with open(r"F:\Ce-shi\zdl_po2019927\config\pageproject.json", 'r', encoding='utf-8')as f:
            pageproject = json.loads(f.read())
            pageobj_value = pageproject['login']['zhiwei']
            zd_id = pageobj_value[0]
            zd_value = pageobj_value[1]
            elementobj = ge(self.driver,zd_id, zd_value)
            return elementobj
if __name__ == '__main__':
    driver = webdriver.Chrome()
    logins = login(driver)


