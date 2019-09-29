
import json
def parseurl(key):
    try:
        with open(r'.\config\url.json') as f:
            content = json.loads(f.read())
            if content:
                if key in content:
                    value = content[key]
                    return value

    except Exception as e:
        print(e)
#获取的url类型的参数

def parselocator(page,element):#
    try:
        with open(r".\config\map.json",'r') as f:
            content = json.loads(f.read())
            if content:
                if page in content:
                    if element in content[page]:
                        return content[page][element]
    except Exception as e:
        print(e)

def UserInfo(info):#
    try:
        with open(r".\config\user.json",'r') as f:
            content = json.loads(f.read())
            if content:
                if info in content:
                    value = content[info]
                    return value
    except Exception as e:
        print(e)


if __name__ == "__main__":
    url = parseurl("url")
    print(url)