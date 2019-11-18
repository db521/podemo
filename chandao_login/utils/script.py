import json

def script(file):
    with open('./config/'+file+'.json', 'r+', encoding='utf-8')as f:
        info = json.loads(f.read())
    return info