from model.login import LoginSetup
from selenium import webdriver
import json

def chadaoZen():
    try:
        driver = webdriver.Chrome()
        with open('../config/urls.json','r') as f:
            wz = json.loads(f.read())
        url = wz["url"]
        driver.get(url)

        with open('../config/user.json','r') as f:
            us = json.loads(f.read())
        name = us["user"]
        passwd = us["passwd"]
        LoginSetup(driver,name,passwd)
    except Exception as e:
        raise e


if __name__ == '__main__':
    chadaoZen()
