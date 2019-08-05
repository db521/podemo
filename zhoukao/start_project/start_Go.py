import json
from selenium import webdriver
from moudle.To_lo import To_log


def start_project():

    try:
        with open('D:\PO\zhoukao\config\\url.json','r') as f:
            url = json.loads(f.read())['url']

            driver = webdriver.Chrome()
            driver.get(url)
            driver.maximize_window()
            To_log(driver)

    except Exception as e:
        raise e


if __name__ == '__main__':
    start_project()
