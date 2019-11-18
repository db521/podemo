import json
from util.wait import getElementImplicitWait as ge
def objs(driver,key1,key2):
    try:
        with open('../config/pageobject.json', 'r', encoding='utf-8') as f:
            sw = json.loads(f.read())
        ss = sw[key1][key2]
        locatetype = ss[0]
        locatorExpression = ss[1]
        elemetObj = ge(driver, locatetype, locatorExpression)
        return elemetObj
    except Exception as e:
        raise e