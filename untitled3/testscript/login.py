from moudle.login import loginStep
import json
from selenium import webdriver

def testLoginZentao():
    try:
        driver=webdriver.Chrome()
        with open('../config/urls.json','r+') as f:
            sw=json.loads(f.read())
        url=sw["url"]
        driver.get(url)

        with open('../config/user.json','r+') as f:
            sw=json.loads(f.read())
        name=sw["name"]
        passwd=sw["passwd"]
        loginStep(driver,name,passwd)

    except Exception as e:
        raise e

