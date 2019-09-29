import json
from module.login import loginStep
from selenium import webdriver
def testloginZentao():
    try:
        driver=webdriver.Chrome()
        with open('../config/config.json','r',encoding='utf-8') as f:
            w=json.loads(f.read())
        url1=w['url']
        driver.get(url1)
        loginStep(driver)
    except Exception as e:
        raise e
if __name__ == '__main__':
    testloginZentao()
