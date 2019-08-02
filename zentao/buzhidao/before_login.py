# -*- coding: utf-8 -*-

import json

from moudle.switch_login import switch_Login
from selenium import webdriver


def before_login():
    """
    具体测试流程，调用moudle模块的操作步骤
    :return:
    """

    try:
        driver = webdriver.Chrome()
        with open('D:\\PO\\zentao\\config\\urls.json','r') as f:
            w = json.loads(f.read())
            url = w["url"]
            driver.get(url)
            driver.maximize_window()
            switch_Login(driver)

    except Exception as e:
        raise e

if __name__ == '__main__':
    before_login()
