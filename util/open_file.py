import json
def open_file(path):
    with open('../config/{}.json'.format(path), 'r+',encoding='utf-8')as f:
        w = json.loads(f.read())
        return w