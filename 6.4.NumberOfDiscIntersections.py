# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 10:21:04 2017

@author: James
"""

"""
6.4.NumberOfDiscIntersections
Compute the number of intersections in a sequence of discs.
"""

import unittest

import bisect

def solution(A):
    # write your code in Python 2.7
    leftPointDict = {}
    for i in range(len(A)):
        a = i - A[i]
        if a in leftPointDict:
            leftPointDict[a] = leftPointDict[a] + 1
        else:
            leftPointDict[a] = 1
    
    leftPointList = [key for key in leftPointDict]
    leftPointList.sort()
    
    preSumDict = {}
    
    s = 0
    for i in range(len(leftPointList)):
        s = s + leftPointDict[leftPointList[i]]
        preSumDict[leftPointList[i]] = s
    
    total = 0
    
    for i in range(len(A)):
        right = bisect.bisect_right(leftPointList, i + A[i])
        right = right - 1
        
        total = total + preSumDict[leftPointList[right]] - preSumDict[i - A[i]] + leftPointDict[i - A[i]] -1
        
    for key in leftPointDict:
        if leftPointDict[key] > 1:
            total = total - leftPointDict[key] * (leftPointDict[key] - 1) / 2
    
    if total > 10000000:
        return -1
        
    return total
        
class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution([1, 5, 2, 1, 4, 0]), 11)
  
        
if __name__ == '__main__':
    unittest.main(exit=False)

