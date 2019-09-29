from po.login import Login
from util.parsejson import parseurl as ul
from util.parsejson import parseuser as pu

def login(a):
    Login(a).zentao().click()
    content = pu()
    Login(a).user().send_keys(content[0])
    Login(a).pwd().send_keys(content[1])
    Login(a).dengluanniu().click()

if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get(ul("url"))
    login(a=driver)