# -*- coding: utf-8 -*-
import json
def parseurl(key):
    try:
        with open(r'F:\bkui\polx\config\url.json','r')as f:
            content=json.loads(f.read())
            if content:
                if key in content:
                    value=content[key]
                    return value
    except Exception as e:
        print(e)
#   解析选择器
def parselocator(page,element):
    try:
        with open(r'F:\bkui\polx\config\map.json','r')as f:
            content=json.loads(f.read())
            if content:
                if page in content:
                    if element in content[page]:
                        return content[page][element]
    except Exception as e:
        print(e)
#         账号
def parseloginuser(key):
    try:
        with open(r'F:\bkui\polx\config\user.json', 'r')as f:
            content = json.loads(f.read())
            user=content["user"]
            return user
    except Exception as e:
        print(e)
#         获取密码
def parseloginpwd(key):
    try:
        with open(r'F:\bkui\polx\config\user.json', 'r')as f:
            content = json.loads(f.read())
            pwd=content["pwd"]
            return pwd
    except Exception as e:
        print(e)
if __name__ == '__main__':
    url=parseurl("url")
    print(url)
    # 获取账号
    user=parseloginuser('user')
    print(type(user))
    #获取密码
    pwd=parseloginpwd('pwd')
    print(pwd)