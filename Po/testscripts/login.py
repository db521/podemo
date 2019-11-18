from module.login import loginStep
import json
from selenium import webdriver


def testloginFts():
    try:
        driver = webdriver.Chrome()
        # 读取URL地址
        with open("../config/urls.json", 'r') as f:
            urls = json.loads(f.read())
        url = urls['url']
        # 发起请求
        driver.get(url)

        # 读取用户名密码
        with open("../config/user.json", 'r') as f:
            uspa = json.loads(f.read())
        name = uspa["user"]
        passwd = uspa["passwd"]

        loginStep(driver, name, passwd)

    except Exception as e:
        raise e


if __name__ == '__main__':
    testloginFts()