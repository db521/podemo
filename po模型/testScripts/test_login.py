from selenium import webdriver
from pageobjects.logins import login
from module.mod import loginStep
import json

def logins():
    try:
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        with open("../config/url.json","r+",encoding="utf-8") as f:
            ss=json.loads(f.read())
        url_id=ss["url"]
        driver.get(url_id)
        loginStep(driver)
    except EnvironmentError as e:
        raise e

if __name__ =="__main__":
    logins()





