from utils.wait import XianShiAndFind as xs
from utils.read_json import read_useradd as ru

class Useradd():
    def __init__(self,driver):
        self.driver=driver
    def username(self):
        try:
            name=ru('username')
            fangFa = name[0]
            biaoDaoShi = name[1]
            elementobj=xs(self.driver,fangFa,biaoDaoShi)
            return elementobj
        except Exception as e:
            print(e)

    def password(self):
        try:
            name=ru('password')
            fangFa = name[0]
            biaoDaoShi = name[1]
            elementobj=xs(self.driver,fangFa,biaoDaoShi)
            return elementobj
        except Exception as e:
            print(e)

    def password2(self):
        try:
            name=ru('password2')
            fangFa = name[0]
            biaoDaoShi = name[1]
            elementobj=xs(self.driver,fangFa,biaoDaoShi)
            return elementobj
        except Exception as e:
            print(e)

    def name(self):
        try:
            name=ru('name')
            fangFa = name[0]
            biaoDaoShi = name[1]
            elementobj=xs(self.driver,fangFa,biaoDaoShi)
            return elementobj
        except Exception as e:
            print(e)

    def zhiwei(self):
        try:
            name=ru('zhiwei')
            fangFa = name[0]
            biaoDaoShi = name[1]
            elementobj=xs(self.driver,fangFa,biaoDaoShi)
            return elementobj
        except Exception as e:
            print(e)

    def group(self):
        try:
            name=ru('group')
            fangFa = name[0]
            biaoDaoShi = name[1]
            elementobj=xs(self.driver,fangFa,biaoDaoShi)
            return elementobj
        except Exception as e:
            print(e)

    def email(self):
        try:
            name=ru('email')
            fangFa = name[0]
            biaoDaoShi = name[1]
            elementobj=xs(self.driver,fangFa,biaoDaoShi)
            return elementobj
        except Exception as e:
            print(e)

    def yuser(self):
        try:
            name=ru('yuser')
            fangFa = name[0]
            biaoDaoShi = name[1]
            elementobj=xs(self.driver,fangFa,biaoDaoShi)
            return elementobj
        except Exception as e:
            print(e)

    def ypasswd(self):
        try:
            name=ru('ypasswd')
            fangFa = name[0]
            biaoDaoShi = name[1]
            elementobj=xs(self.driver,fangFa,biaoDaoShi)
            return elementobj
        except Exception as e:
            print(e)

    def sver(self):
        try:
            name=ru('sver')
            fangFa = name[0]
            biaoDaoShi = name[1]
            elementobj=xs(self.driver,fangFa,biaoDaoShi)
            return elementobj
        except Exception as e:
            print(e)

    def zuzhi(self):
        try:
            name=ru('zuzhi')
            fangFa = name[0]
            biaoDaoShi = name[1]
            elementobj=xs(self.driver,fangFa,biaoDaoShi)
            return elementobj
        except Exception as e:
            print(e)

    def useradd(self):
        try:
            name=ru('useradd')
            fangFa = name[0]
            biaoDaoShi = name[1]
            elementobj=xs(self.driver,fangFa,biaoDaoShi)
            return elementobj
        except Exception as e:
            print(e)