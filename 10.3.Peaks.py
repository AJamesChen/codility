"""
10.3.Peaks
Divide an array into the maximum number of same-sized blocks, each of which should contain an index P such that A[P - 1] < A[P] > A[P + 1].
"""

import unittest

def solution(A):
    # write your code in Python 2.7
    i = 1
    factors = []
    N = len(A)
    
    while i * i <= N:
        if N % i == 0:
            if i != N // i:
                factors.append(N // i)
            factors.append(i)
        i = i + 1
        
    factors.sort()
    
    peaks = len(A) * [0]
    totalPeaks = 0
    for i in range(N):
        if i - 1 >= 0 and i + 1 < N:
            if A[i - 1] < A[i] and A[i] > A[i + 1]:
                peaks[i] = 1
                totalPeaks = totalPeaks + 1
    
    if totalPeaks < 2:
        return totalPeaks
        
    preSumPeaks = [0]
    for i in range(N):
        preSumPeaks.append(preSumPeaks[i] + peaks[i])
    
    for i in range(1, len(factors)):
        
        if totalPeaks < N // factors[i]:
            continue
        
        hasPeak = True
        
        for j in range(factors[i], N, factors[i]):
            if preSumPeaks[j] == preSumPeaks[j - factors[i]]:
                hasPeak = False
                break
            
            if totalPeaks - preSumPeaks[j] < (N - j) // factors[i]:
                hasPeak = False
                break
        
        if hasPeak:
            return N // factors[i]
    
    return 0
        
class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution([1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]), 3)
  
        
if __name__ == '__main__':
    unittest.main(exit=False)
