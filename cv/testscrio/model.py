import  json
from selenium import webdriver

from models.login import loginclick
def testlogin():
    dirver = webdriver.Chrome('E:\英雄时刻\chromedriver')
    with open('../config/url.json','r')as f:
        connt=json.loads(f.read())



    url = connt["url"]

    dirver.get(url)
    loginclick(dirver)


if __name__=='__main__':
    testlogin()

