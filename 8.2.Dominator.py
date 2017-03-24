"""
8.2.Dominator
Find an index of an array such that its value occurs at more than half of indices in the array.
"""

import unittest

def solution(A):
    # write your code in Python 2.7
    d = {}
    for i in range(len(A)):
        if A[i] in d:
            d[A[i]] = d[A[i]] + 1
        else:
            d[A[i]] = 1
        
        if d[A[i]] > len(A) / 2:
            return i
    
    return -1
        
class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution([8, 0]), -1)
        self.assertEqual(solution([3, 4, 3, 2, 3, -1, 3, 3]), 7)
        
if __name__ == '__main__':
    unittest.main(exit=False)
