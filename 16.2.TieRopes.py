# -*- coding: utf-8 -*-
"""
@author: James
"""

"""
16.2.TieRopes
COMMENT VIEW  START
Tie adjacent ropes to achieve the maximum number of ropes of length >= K.
https://codility.com/demo/results/trainingQV5EE9-A33/
"""

import unittest

def solution(K, A):
    # write your code in Python 2.7
    R = 0
    s = 0
    for a in A:
        s = s + a
        if s >= K:
            R = R + 1
            s = 0
    return R
        
class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution(4, [1, 2, 3, 4, 1, 1, 3]), 3)
  
if __name__ == '__main__':
    unittest.main(exit=False)
