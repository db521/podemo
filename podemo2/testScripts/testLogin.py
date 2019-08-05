import json

from modules.login import LoginSup
from selenium import webdriver


def testlogin():
    try:

        driver = webdriver.Chrome()
        with open('../config/config.json', 'r+')as f:
            w = json.loads(f.read())
        url = w['url']
        driver.get(url)
        LoginSup(driver)
    except Exception as e:
        raise e


if __name__ == '__main__':
    testlogin()
