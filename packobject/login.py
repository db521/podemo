# -*- coding: utf-8 -*-
from selenium import webdriver
import json

class login:
    def __init__(self):
        self.driver = webdriver

    def btnobj(self):
        try:
            with open(r'D:\works\untitled13\config\demo.json','r') as f:
                content = json.loads(f.read())
                print(content)
        except Exception as e:
            print(e)