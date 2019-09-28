
from utils.wait import XianShiAndFind as xs
from utils.read_json import read_config as rc
class Login_page():
    def __init__(self,driver):
        self.driver = driver
    def usename(self):
        try:
            name=rc('json')['username']
            fangFa = name[0]
            biaoDaoShi = name[1]
            elementobj=xs(self.driver,fangFa,biaoDaoShi)
            return elementobj
        except Exception as e:
            print(e)
    def passwd(self):
        try:
            pd=rc('json')['password']
            fangFa = pd[0]
            biaoDaoShi = pd[1]
            elementobj=xs(self.driver,fangFa,biaoDaoShi)
            return elementobj
        except Exception as e:
            print(e)
    def button(self):
        try:
            bu=rc('json')['button']
            fangFa = bu[0]
            biaoDaoShi = bu[1]
            elementobj=xs(self.driver,fangFa,biaoDaoShi)
            return elementobj
        except Exception as e:
            print(e)
