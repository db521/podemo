import json
from selenium import webdriver
from module.login import loginStep
def test_login():
    try:
        driver=webdriver.Chrome()
        with open("../config/url.json","r+",encoding="utf-8")as f:
            w = json.loads(f.read())
        url = w["url"]
        driver.get(url)

        with open("../config/user.json","r+",encoding="utf-8")as f:
            w=json.loads(f.read())
        user=w["user"]
        passwd=w["passwd"]
        loginStep(driver,user,passwd)
    except Exception as e:
        raise e

if __name__ == '__main__':
    test_login()
