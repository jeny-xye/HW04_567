"""
HW04a test
Author: Xinyi Ye
Date: 02/18/2020
"""
from HW04a_Xinyi_Ye import find_re
import unittest


class TestRE(unittest.TestCase):
    """ test class """
    def test_find_re(self):
        id1 = 'richkempinski'
        
        result_1 = [['hellogitworld', 30], ['helloworld', 6],
                    ['Mocks', 10], ['Project1', 2], ['threads-of-life', 1]]
        self.assertTrue(find_re(id1) == result_1)
        


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
