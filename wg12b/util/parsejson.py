import json

def parseurl(key):
    try:
        with open(r"D:\学习\test—1\wg12b\config\url.json", "r") as f:
            conrent = json.loads(f.read())
            if conrent:
                if key in conrent:
                    value = conrent[key]
                    return value
    except Exception as e:
        print(e)

def parseuser(key):
    try:
        with open(r"D:\学习\test—1\wg12b\config\user.json", "r") as f:
            conrent = json.loads(f.read())
            if conrent:
                if key in conrent:
                    value = conrent[key]
                    return value
    except Exception as e:
        print(e)

def parselocator(page,element):
    try:
        with open(r"D:\学习\test—1\wg12b\config\map.json", "r") as f:
            conrent = json.loads(f.read())
            if conrent:
                if page in conrent:
                    if element in conrent[page]:
                        return conrent[page][element]
    except Exception as e:
        print(e)

def parsename(page,element):
    try:
        with open(r"../config/user.json", "r") as f:
            conrent = json.loads(f.read())
            if conrent:
                if page in conrent:
                    if element in conrent[page]:
                        return conrent[page][element]
    except Exception as e:
        print(e)

if __name__ == '__main__':
    url = parseuser("passwd")
    print(url)