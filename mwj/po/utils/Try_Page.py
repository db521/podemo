import json

def Try_Page(driver,pathjson,locatetype,locatevalues,page):
    try:
        with open(pathjson, "r", encoding='utf-8') as f:
            ds = json.loads(f.read())
        ss = ds[locatetype][locatevalues]
        typ = ss[0]
        lj = ss[1]
        element = page(driver, typ, lj)
        return element

    except Exception as e:
        raise e