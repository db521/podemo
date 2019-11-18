import time
import json
from modlue.login import longinstep
from selenium import webdriver


def getsport():
    try:
        dr = webdriver.Chrome()
        with open('../config/urls.json','r',encoding='utf-8') as f:
            u = json.loads(f.read())
        url = u["url"]
        dr.get(url)
        with open('../config/user.json','r',encoding='utf-8') as f:
            us = json.loads(f.read())
        name = us["name"]
        password = us["password"]
        longinstep(dr,name,password)
        time.sleep(5)
    except Exception as e:
        raise e

if __name__ == '__main__':
    getsport()