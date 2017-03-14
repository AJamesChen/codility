"""
1. CyclicRotation
Rotate an array to the right by a given number of steps.
"""

import unittest

def solution(A, K):
    # write your code in Python 2.7
    if len(A) == 0:
        return A
    
    L = len(A)
    
    if K % L != 0:
        K = K % L
        A.extend(A[0 : L - K])
        A[0 : L - K] = []
    
    return A

class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution([3, 8, 9, 7, 6], 1),  [6, 3, 8, 9, 7])
        self.assertEqual(solution([1], 1), [1])
        self.assertEqual(solution([1, 2], 1), [2, 1])
        self.assertEqual(solution([1, 2], 2), [1, 2])
        self.assertEqual(solution([], 1), [])
if __name__ == '__main__':
    unittest.main(exit=False)
