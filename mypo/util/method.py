import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
def open_file(path):
    try:
        with open('../config/{}'.format(path),'r',encoding='utf-8')as f:
            content=json.loads(f.read())
        return content
    except Exception as e:
        raise e

def get_find_element(driver,type,value):
    try:
        element=WebDriverWait(driver,10).until(lambda x:x.find_element(eval(type),value))
        return element
    except Exception as e:
        raise e

def element_obj(driver,file,key1,key2):
    try:
        value_list=file[key1][key2]
        type=value_list[0]
        value=value_list[1]
        element=get_find_element(driver,type,value)
        return element
    except Exception as e:
        raise e