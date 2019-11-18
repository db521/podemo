

from selenium.webdriver.common.by import By
from selenium import webdriver
dr=webdriver.Chrome()
dr.get('https://www.baidu.com/')
dr.find_element(eval('By.LINK_TEXT'),'地图').click()