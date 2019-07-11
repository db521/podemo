import json

with open('pageobject.json',mode="r") as f:
    a = json.loads(f.read())
    print(a)