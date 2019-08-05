import json

from module.login import loginStep
from selenium import webdriver

def testloginzentao():
    try:
        driver = webdriver.Chrome()
        with open(r'D:\pachong2\podemo_1\config\config.json','r+',encoding='utf-8') as f:
            dicts = json.loads(f.read())
        url = dicts["url"]
        driver.get(url)
        loginStep(driver)
    except Exception as e:
        raise e




