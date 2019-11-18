from util.open_file import open_file
from util.obj import obj
class Add:
    def __init__(self, driver):
        self.driver = driver
        self.sw = open_file('pageobject')
    def bumen_obj(self):
        try:
            return obj(self.driver,self.sw,'add_bumen','click_group')
        except Exception as e:
            raise e

    def zuzhi_obj(self):
        try:
            return obj(self.driver,self.sw,'add_bumen','click_bumen')
        except Exception as e:
            raise e
    def input_obj(self):
        try:
            return obj(self.driver,self.sw,'add_bumen','input_bumen')
        except Exception as e:
            raise e

    def submit_obj(self):
        try:
            return obj(self.driver,self.sw,'add_bumen','submit')
        except Exception as e:
            raise e
