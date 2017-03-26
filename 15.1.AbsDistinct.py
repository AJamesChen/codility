# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 10:21:04 2017

@author: James
"""

"""
15.1.AbsDistinct
Compute number of distinct absolute values of sorted array elements.
https://codility.com/demo/results/trainingR2JNQZ-KUT/
"""

import unittest

def solution(A):
    # write your code in Python 2.7
    S = set(abs(a) for a in A)
    return len(S)
        
class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution([-5, -3, -1, 0, 3, 6]), 5)
  
        
if __name__ == '__main__':
    unittest.main(exit=False)


