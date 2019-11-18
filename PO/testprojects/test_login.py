from module.login import loginStep
import json

def test_login():
    try:
        from selenium import webdriver
        with open("../config/url.json",'r')as f:
            ss = json.loads(f.read())
        url=ss["url"]
        driver=webdriver.Chrome()
        driver.get(url)
        with open("../config/user.json","r")as f:
            ss=json.loads(f.read())
        user=ss["user"]
        passwd=ss["passwd"]
        loginStep(driver,user,passwd)
    except Exception as e:
        raise e
if __name__ == '__main__':
    test_login()