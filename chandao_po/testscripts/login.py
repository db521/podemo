#coding=utf-8;
import json
from model.login import login_step
from selenium import webdriver
def testloginZentao():
    driver=webdriver.Chrome(r"F:\Ce-shi\chandao_po\chromedriver.exe")
    with open(r'F:\Ce-shi\chandao_po\config\config.json','r',encoding='utf-8')as f:
        config_url=json.loads(f.read())
        url=config_url['url']
        driver.get(url)
        login_step(driver) 
if __name__ == '__main__':
    testloginZentao()
