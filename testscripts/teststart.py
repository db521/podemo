import  json
from pageobject.login import login
from selenium import webdriver

def test_start():
    try:
        driver=webdriver.Chrome()
        with open(r'C:\Users\Lenovo\Desktop\zendao\config\url.json','r',encoding='utf-8') as f:
            dicts=json.loads(f.read())
        url=dicts['url']
        driver.get(url)
        login(driver)
    except Exception as e:
        raise e
