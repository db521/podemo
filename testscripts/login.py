# -*- coding: utf-8 -*-
# import vie,ser,oth,mod,url
import json

from module.login import loginStep
from selenium import webdriver

def testloginzentao():
    try:
        driver = webdriver.Chrome()
        with open(r'F:\po\podemo_1\config\config.json','r+',encoding='utf-8') as f:
            dicts = json.loads(f.read())
        url = dicts["url"]
        driver.get(url)
        loginStep(driver)
    except Exception as e:
        raise e




