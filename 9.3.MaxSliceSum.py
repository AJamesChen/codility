"""
9.3.MaxSliceSum
Find a maximum sum of a compact subsequence of array elements.
"""

import unittest

def solution(A):
    # write your code in Python 2.7
    s = 0
    m = -1000000
    
    for a in A:
        s = s + a
        m = max(m, s)
        if s < 0:
            s = 0
    
    return m
        
class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution([8, 0]), 8)
        self.assertEqual(solution([3, 2, -6, 4, 0]), 5)
        
if __name__ == '__main__':
    unittest.main(exit=False)

