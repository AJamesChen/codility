# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 10:21:04 2017

@author: James
"""

"""
9.1. MaxDoubleSliceSum
Find the maximal sum of any double slice.
https://codility.com/demo/results/trainingUMHPCK-RC4/
"""

import unittest

def solution(A):
    N = len(A)
    maxToSlice = N * [0]
    s = 0
    for i in range(1, N - 1):
        if i == 1:
            s = 0
        else:
            s = s + A[i - 1]
        if s < 0:
            s = 0
        
        maxToSlice[i] = s
    
    
    maxFromSlice = N * [0]
    s = 0
    for i in range(-2, -N, -1):
        if i == -2:
            s = 0
        else:
            s = s + A[i + 1]
        if s < 0:
            s = 0
        maxFromSlice[i] = s
        
    maxSum = -10000
    
    for i in range(1, N -1):
        maxSum = max(maxSum, maxFromSlice[i] + maxToSlice[i])
    
    return maxSum
        
class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution([3, 2, 6, -1, 4, 5, -1, 2]), 17)
  
        
if __name__ == '__main__':
    unittest.main(exit=False)

