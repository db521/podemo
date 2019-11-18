from util.Try_Page import *
from util.wait import GetWebDriverWait as ge

class Del:

    def __init__(self,driver):
        self.driver=driver

    def DelObj(self):
        return Try_Page(self.driver,"./config/pageobject.json","del_bumen","del",ge)

