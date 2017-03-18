"""
6.1.Distinct
Compute number of distinct values in an array.
"""
import unittest

def solution(A):
    # write your code in Python 2.7
    return len(set(A))

class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution([2, 1, 1, 2, 3, 1]),  3)
        
if __name__ == '__main__':
    unittest.main(exit=False)
