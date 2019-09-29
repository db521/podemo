from selenium import webdriver
from module.login import login as log
from util.parsejson import parseurl as pu

def testlog():
    dr = webdriver.Chrome()
    url = pu("url")
    dr.get(url)
    log(driver=dr)

if __name__ == '__main__':
    testlog()
