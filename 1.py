import json

with open(r"D:\测试\PO\config\url.json","r")as f:
    content = json.loads(f.read())
    print(type(content))