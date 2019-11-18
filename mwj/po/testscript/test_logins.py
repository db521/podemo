from moudle.login import loginsUp
import json

def testlog():
    try:
        from selenium import webdriver
        driver = webdriver.Chrome()
        with open('./config/urls.json','r') as f:
            ul = json.loads(f.read())
        driver.get(ul["urls"])

        with open('./config/user.json','r') as f:
            up = json.loads(f.read())
            # print(up)
        loginsUp(driver,up["user"],up["passwd"],up['bumen'])


    except Exception as e:
        raise e