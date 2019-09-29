import json
import os


def parseurl(key):
    try:
        with open(r"D:\workspace\PO\config\url.json", 'r') as f:
            content = json.loads(f.read())
            if content:
                if key in content:
                    value=content[key]
                    return value
    except Exception as e:
        print(e)

def parselocator(page,element):
    try:
        with open(r".\config\map.json", 'r') as f:
            content = json.loads(f.read())
            if content:
                if page in content:
                    if element in content[page]:
                        return content[page][element]
    except Exception as  e:
        print(e)


if __name__ == '__main__':
    url=parseurl("url")
    print(url)