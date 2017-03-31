# -*- coding: utf-8 -*-
"""
Created on Sat Apr 01 09:11:33 2017

@author: James
"""

"""
10.4.Flags
Find the maximum number of flags that can be set on mountain peaks.
"""

import unittest

import bisect

def solution(A):
    # write your code in Python 2.7
    N = len(A)
    peaks = N * [0]
    totalPeaks = 0
    preSum = N * [0]
    firstPeakPos = 0
    lastPeakPos = 0
    for i in range(1, N -1):
        if A[i - 1] < A[i] and A[i] > A[i + 1]:
            peaks[i] = 1
            totalPeaks = totalPeaks + 1
            if firstPeakPos == 0:
                firstPeakPos = i
            lastPeakPos = i
            
        preSum[i] = totalPeaks
    preSum[N - 1] = totalPeaks
    
    if totalPeaks < 2:
        return totalPeaks
    
    distance = lastPeakPos - firstPeakPos
    j = 1
    while j * (j - 1) < distance:
        j = j + 1
    
    if j * (j - 1) != distance:
        j = j - 1
    
    maxFlags = min(j, totalPeaks)

    while maxFlags > 1:
        k = firstPeakPos
        flags = 1
        while k + maxFlags < N:
            if peaks[k + maxFlags] != 1:
                k = bisect.bisect_left(preSum, preSum[k + maxFlags] + 1, k + maxFlags)
                if k == N:
                    break
            else:
                k = k + maxFlags
            flags = flags + 1
            
            if flags == maxFlags:
                return maxFlags
            
            # if there is not enough peaks left
            if maxFlags - flags > totalPeaks - preSum[k]:
                break
        
        maxFlags = maxFlags - 1
    
    return maxFlags
        
class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution([1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]), 3)
  
if __name__ == '__main__':
    unittest.main(exit=False)
