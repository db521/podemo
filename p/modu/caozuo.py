from po.fengzhuang import Login
def denglu(driver,name,passwd):
    try:
        logins=Login(driver)
        logins.name().send_keys(name)
        logins.passwd().send_keys(passwd)
        logins.btn().click()


    except Exception as e:
        print(e)
if __name__ == '__main__':
    pass