import json

def ele_single(locate,locate_exp):
    with open('./config/pageobj.json', 'r+', encoding='utf-8')as f:
        info = json.loads(f.read())
    li = info[locate][locate_exp]
    return li