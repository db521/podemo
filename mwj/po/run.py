import unittest
from testscript.test_logins import testlog
from BeautifulReport import BeautifulReport

class Test_cat(unittest.TestCase):

    def setUp(self):
        pass
    def test_zen(self):
        testlog()

    def tearDown(self):
        pass

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test_cat))
    result = BeautifulReport(suite)
    result.report(filename='禅道',description='详细',report_dir='report')