from selenium import webdriver
import json
from module.module import logStep

def testlogin():
    try:
        with open(r'D:\Python\Django\week1\config\config.json', "r+", encoding="utf8") as f:
            js = json.loads(f.read())
        url = js['url']
        driver = webdriver.Chrome()
        driver.get(url)
        logStep(driver)
    except Exception as e:
        raise e



if __name__ == "main":
    testlogin()

