import json
def read_config(key):
    try:
        with open(r"C:\Users\lenovo\PycharmProjects\pomod\config\loginconfig.json", "r", encoding="utf-8") as f:
            sw = json.loads(f.read())
        if sw:
            if key in sw :
                return sw[key]
    except Exception as e:
        print(e)
def read_url(key):
    try:
        with open(r"C:\Users\lenovo\PycharmProjects\pomod\config\urls.json", "r", encoding="utf-8") as f:
            sw = json.loads(f.read())
        if sw:
            if key in sw :
                return sw[key]
    except Exception as e:
        print(e)

def read_user(key):
    try:
        with open(r"C:\Users\lenovo\PycharmProjects\pomod\config\users.json", "r", encoding="utf-8") as f:
            sw = json.loads(f.read())
        if sw:
            if key in sw :
                return sw[key]
    except Exception as e:
        print(e)

def read_useradd(key):
    try:
        with open(r"C:\Users\lenovo\PycharmProjects\pomod\config\useradd.json", "r", encoding="utf-8") as f:
            sw = json.loads(f.read())
        if sw:
            if key in sw :
                return sw[key]
    except Exception as e:
        print(e)