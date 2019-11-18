from util.method import *
def user_obj(driver,file):
    try:
        return element_obj(driver,file,'login','name')
    except Exception as e:
        raise e

def passwd_obj(driver,file):
    try:
        return element_obj(driver,file,'login','passwd')
    except Exception as e:
        raise e

def submit_obj(driver,file):
    try:
        return element_obj(driver,file,'login','btn')
    except Exception as e:
        raise e
