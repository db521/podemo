from PO.pageobj import login
from selenium import webdriver
def logStept(driver,user,passwd):
    logins=login(driver)
    logins.nameobj().send_keys(user)
    logins.passwdobj().send_keys(passwd)
    logins.submitobj().click()

# if __name__ == '__main__':
#     driver=webdriver.Chrome()
#     log=login(driver)
#     user=log.nameobj()
#     passwd=log.passwdobj()
#     submit=log.submitobj()
#     logStept(driver,user,passwd)
