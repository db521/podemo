import unittest
from BeautifulReport import BeautifulReport

if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTests(unittest.defaultTestLoader.discover('./cases'))
    BeautifulReport(suit).report(description='禅道登录', filename="report.html",report_dir='./report')
