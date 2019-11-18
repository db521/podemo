import json

def Try_Test(pathjson):
    try:
        with open(pathjson,"r+",encoding="utf-8")as f:
            w=json.loads(f.read())
        return w
    except Exception as e:
        raise e