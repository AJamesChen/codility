"""
6.2.MaxProductOfThree
Maximize A[P] * A[Q] * A[R] for any triplet (P, Q, R).
"""
import unittest

def solution(A):
    # write your code in Python 2.7
    A.sort()
    
    if A[1] >= 0:
        return A[-1] * A[-2] * A[-3]
    else:
        return max(A[0] * A[1] * A[-1], A[-3] * A[-2] * A[-1])

class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution([-3, 1, 2, -2, 5, 6]), 60)
        
if __name__ == '__main__':
    unittest.main(exit=False)
