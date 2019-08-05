import json
from selenium import webdriver
from ..module.login import loginstep
def testlogin():
    try:
        driver = webdriver.Chrome()
        with open('D:\pythontest\zk01\config\aa.json' ,'r')as f: w= json.loads(f.read())
        url = w['url']
        driver.get(url)
        loginstep(driver)
    except Exception as e:
        raise e
if __name__ =='__main_ _' :
    testlogin()

