import json
from util.wait import getWait as gw



class login:
    def __init__(self,driver):
        self.driver = driver
    def zhangHkuang(self):
        try:
            with open('../config/pageobject.json', 'r', encoding='utf-8')as f:
                sj = json.loads(f.read())
            ss = sj['login']['name']
            shuj1 = ss[0]
            shuj2 = ss[1]
            elementObj = gw(self.driver,shuj1,shuj2)
            return elementObj
        except Exception as e:
            raise e
    def miMkuang(self):
        try:
            with open('../config/pageobject.json', 'r', encoding='utf-8')as f:
                sj = json.loads(f.read())
            ss = sj['login']['passwd']
            shuj1 = ss[0]
            shuj2 = ss[1]
            elementObj = gw(self.driver,shuj1,shuj2)
            return elementObj
        except Exception as e:
            raise e
    def dengLanniu(self):
        try:
            with open('../config/pageobject.json', 'r', encoding='utf-8')as f:
                sj = json.loads(f.read())
            ss = sj['login']['btn']
            shuj1 = ss[0]
            shuj2 = ss[1]
            elementObj = gw(self.driver,shuj1,shuj2)
            return elementObj
        except Exception as e:
            raise e
if __name__ == '__main__':
    pass