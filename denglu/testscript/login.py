import json
from module.login import loginS
from selenium import webdriver
import time

def dengLuzenTao():
    try:
        driver = webdriver.Chrome()
        with open('../config/urls.json','r')as f:
            u = json.loads(f.read())
        url = u['url']
        driver.get(url)

        with open('../config/users.json','r')as f:
            u = json.loads(f.read())
        name = u['user']
        passwd = u['passwd']

        loginS(driver,name,passwd)
    except Exception as e:
        raise e

if __name__ == '__main__':
    dengLuzenTao()
