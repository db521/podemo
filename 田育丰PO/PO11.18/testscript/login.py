from PO.pageobj import login
from module.login import logStept
from selenium import webdriver
import time
import json

def zenTao():
    try:
        driver=webdriver.Chrome()
        a=login(driver)
        url=a.urlobj()
        driver.get(url["url"])
        with open('../config/username.json','r') as f:
            e=json.loads(f.read())
            username=e["user"]
            passwd=e["passwd"]



        logStept(driver,username,passwd)
        time.sleep(5)
        driver.quit()
    except Exception as e:
        raise e
if __name__ == '__main__':
    zenTao()