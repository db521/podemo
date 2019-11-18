import json

def Try_Test(jsonpath):
    """

    :param jsonpath:
    :return:
    传入文件路径
    """
    try:
        with open(jsonpath,'r',encoding='utf-8') as f:
            w = json.loads(f.read())
        return w
    except Exception as e:
        raise e