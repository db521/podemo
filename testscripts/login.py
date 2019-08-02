from selenium import webdriver
import json
from module.login import loginStep

def testlogin():
    try:
        driver = webdriver.Chrome()
        with open("D:\Python\Django\lianxi\config\config.json","r+",encoding='utf8') as f:
            js = json.loads(f.read())

        url = js["url"]
        driver.get(url)

        loginStep(driver)

    except Exception as e:
        raise e

if __name__ =="__main__":
        testlogin()