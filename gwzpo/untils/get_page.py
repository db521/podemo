import json

def get_page(driver,jsonpath,objkey,objvalue,page):
    """
    :param driver:
    :param jsonpath:
    :param objkey:
    :param objvalue:
    :param page:
    :return:
    相当于一个读文件内容的工具，方便页面定位的调用
    """
    try:
        with open(jsonpath,'r',encoding='utf-8') as f:
            objs = json.loads(f.read())
        obj = objs[objkey][objvalue]
        locatetype = obj[0]
        locatevalue = obj[1]
        element = page(driver,locatetype,locatevalue)
        return element

    except Exception as e:
        raise e