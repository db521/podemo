import json

def Try_Page(driver,pathjson,objkey,objvalue,page):
    try:
        with open(pathjson,"r+",encoding="utf-8")as f:
            objs=json.loads(f.read())
        obj=objs[objkey][objvalue]
        elementObj=page(driver,obj[0],obj[1])
        return elementObj
    except Exception as e:
        raise e