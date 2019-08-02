import json
from selenium import webdriver

def  loginZentao():
    try:
        driver = webdriver.Chrome()


        with open('F:\yuekao111\config\configs.json','r+')as f:
            w = json.loads(f.read())
        url = w['url']
        driver.get(url)
    except Exception as e:
        raise e
if __name__ == '__main__':
    loginZentao()
