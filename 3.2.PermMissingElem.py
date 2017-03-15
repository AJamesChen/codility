"""
 PermMissingElem
Find the missing element in a given permutation.
"""

import unittest

def solution(A):
    # write your code in Python 2.7
    N = len(A) + 1
    return N * (N + 1) / 2 - sum(A)
class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution([2, 3, 1, 5]), 4)
        self.assertEqual(solution([1]), 2)
        self.assertEqual(solution([2]), 1)
if __name__ == '__main__':
    unittest.main(exit=False)

