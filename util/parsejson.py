import  json

def parseurl(key):
    try:
        with open(r"D:\测试\PO\config\url.json","r")as f:
            content = json.loads(f.read())
            if content:
                if key in content:
                    value=content[key]
                    return value
    except Ellipsis as e:
        print(e)


def parsedingwei(page,element):
    try:
        with open(r"D:\测试\PO\config\dingwei.json","r")as f:
            content = json.loads(f.read())
            if content:
                if page in content:
                    if element in content[page]:
                        return content[page][element]
    except Ellipsis as e:
        print(e)

def parseuser():
    with open(r"D:\测试\PO\config\user.json","r")as f:
        content = json.loads(f.read())
        if content:
            username=content["user"]
            password=content["pwd"]
            return username,password



if __name__ == '__main__':
    # url=parseurl("url")
    # print(url)
    user=parseuser()
    print(user)
