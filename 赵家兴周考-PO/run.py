import unittest
from testscripts.test_login_add_del import Test_Login_Add_Del
from BeautifulReport import  BeautifulReport

class Test_Zentao(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_zentao(self):
        Test_Login_Add_Del()

if __name__ == '__main__':
    suite=unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test_Zentao))
    result=BeautifulReport(suite)
    result.report(filename="禅道",description="详细情况如下",report_dir="webreport")