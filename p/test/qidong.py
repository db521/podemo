import json
from modu.caozuo import denglu
from selenium import webdriver
def test_denglu():
    try:
        driver=webdriver.Chrome()
        with open('D:\Django\untitled\p\cofig\cofig.json','r')as f:
            duqu=json.loads(f.read())
            url=duqu["url"]
            driver.get(url)
            denglu(driver,name,passwd)


    except Exception as e:
        print(e)
