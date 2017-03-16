"""
PermCheck
Check whether array A is a permutation.
"""
import unittest

def solution(A):
    # write your code in Python 2.7
    B = set(A)
    m = max(B)
    if len(A) == m and len(A) == len(B):
        return 1
    else:
        return 0

class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution([1, 2, 4, 3]), 1)
        self.assertEqual(solution([3, 1, 2, 4, 3]), 0)
        self.assertEqual(solution([2, 4, 3]), 0)
        
if __name__ == '__main__':
    unittest.main(exit=False)

