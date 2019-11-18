import json
from selenium import webdriver
from moude.moudelogin import logins


def testmode():
    try:
        web=webdriver.Chrome()
        with open('../login/urls.json','r',encoding='utf8')as f:
            po=json.loads(f.read())
        url=po['urlas']
        web.get(url)

        with open('../login/names.json','r',encoding='utf8')as f:
            mx=json.loads(f.read())
        name=mx['user']
        passwd=mx['passwd']
        logins(web,name,passwd)

    except Exception as e:
        raise e

if __name__ == '__main__':
    testmode()