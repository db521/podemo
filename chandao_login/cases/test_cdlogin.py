import unittest
from testscripts.login import login

class CD_test(unittest.TestCase):
    def test_log(self):
        login()