import unittest
import time
from HTMLTestRunnerNew import HTMLTestRunner
# 测试用例目录
test_dir = './testscripts'
#测试用例文件名匹配原则
suits = unittest.defaultTestLoader.discover(test_dir,pattern='test_useradd.py')
if __name__ == '__main__':
    now_time = time.strftime('%Y-%m-%d %H_%M_%S')
    fp = open('C:/Users/lenovo/PycharmProjects/pomod/config/' + now_time + 'result.html', 'wb')
    runner = HTMLTestRunner(stream=fp, title='禅道添加用户测试报告', description='测试环境：Windows 10，chrome')
    runner.run(suits)