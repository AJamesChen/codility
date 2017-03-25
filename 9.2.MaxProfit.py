"""
9.2.MaxProfit
Given a log of stock prices compute the maximum possible earning.
"""

import unittest

def solution(A):
    # write your code in Python 2.7
    if len(A) < 2:
        return 0
    profits = []
    
    for i in range(1, len(A)):
        profits.append(A[i] - A[i - 1])
        
    s = 0
    m = -200000
    
    for i in range(len(profits)):
        s = s + profits[i]
        m = max(m, s)
        
        if s < 0:
            s = 0
    
    if m < 0:
        m = 0
    
    return m
        
class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution([23171, 21011, 21123, 21366, 21367]), 356)
        
if __name__ == '__main__':
    unittest.main(exit=False)

