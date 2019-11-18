from moudle.login import *
from utils.script import script
from selenium import webdriver

def login():

    driver = webdriver.Chrome()
    url = script("urls")['url']
    driver.get(url)
    user = script("users")["login"]['user']
    passwd = script("users")["login"]["passwd"]

    return login_CD(driver=driver,user=user,passwd=passwd)

if __name__ == '__main__':
    login()