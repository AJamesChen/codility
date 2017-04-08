# -*- coding: utf-8 -*-
"""
Created on Sat Apr 08 19:18:59 2017

@author: James
"""
"""
15.4.MinAbsSumOfTwo
Find the minimal absolute value of a sum of two elements.
"""

import unittest

def solution(A):
    # write your code in Python 2.7
    A.extend(A)
        
    A.sort(key = lambda a: abs(a))
    
    m = 2000000000
    for i in range(0, len(A) - 1):
        m = min(abs(A[i] + A[i + 1]), m)
    
    return m
        
class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution([1, 4, -3]), 1)
        self.assertEqual(solution([-8, 4, 5, -10, 3]), 3)
  
if __name__ == '__main__':
    unittest.main(exit=False)
