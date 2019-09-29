# -*- coding: utf-8 -*-
'''
@Time    : 2019/9/28 9:30
@Author  : Allen
@File    : .py
'''

import json
def parseurl(key):
    try:
        with open(r'D:\Pycharm\Code\实训三\PO模型\1613Btest\config\urls.json','r')as f:
            content = json.loads(f.read())
            if content:
                if key in content:
                    value = content[key]
                    return value
    except Exception as e:
        print(e)

def parse_anniu(file,page,element):
    try:
        with open(file,'r')as f:
            content = json.loads(f.read())
            if content:
                if page in content:
                    if element in content[page]:
                        return content[page][element]

    except Exception as e:
        print(e)

def Userinfo(file,key):
    try:
        with open(file,'r')as f:
            content = json.loads(f.read())
            if content:
                if key in content:
                    value = content[key]
                    return value
    except Exception as e:
        print(e)













