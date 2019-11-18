from util.open_file import open_file
from module.add_bumen import add_bm
from testscripts.test_login import Test_login
class Test_adds(Test_login):
    def test_add(self):
        try:
            w=open_file('bumen')
            add_bm(self.driver,w['name'])
        except Exception as e:
            raise e

if __name__ == '__main__':
    adds=Test_adds()
    adds.testloginZentao()
    adds.test_add()