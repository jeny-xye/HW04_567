"""
HW05a test
Author: Xinyi Ye
Date: 02/25/2020
"""
from HW04a_Xinyi_Ye import find_re
import unittest
from unittest.mock import patch



@unittest.mock.patch('requests.get')

def test_find_re(self, mockedReq):     
    mockedReq.return_value = '[["hellogitworld", 30], ["helloworld", 6], ["Mocks", 10], ["Project1", 2], ["threads-of-life", 1]]'                 
    commits = find_re(self.s)
    self.assertEqual(len(commits), 5)
                
        
if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
