from module.login import login as lo
from selenium import webdriver
import json


def login():
    try:
        dr = webdriver.Chrome()
        with open('../config/url.json','r')as f:
            u = json.loads(f.read())
        url = u['url']
        dr.get(url)
        with open('../config/user.json','r')as f:
            user = json.loads(f.read())
        username = user['username']
        password = user['password']
        lo(dr,username,password)



    except Exception as e:
        raise e

if __name__ == '__main__':
    login()