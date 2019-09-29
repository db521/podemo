# -*- coding: utf-8 -*-
import json
from selenium import webdriver
from module.login import Login
from util.parsejson import parseurl as pu
def testloginZentao():
    url=pu("url")
    ba=webdriver.Chrome()
    ba.get(url)