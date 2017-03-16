"""
4.3.MissingInteger
Find the minimal positive integer not occurring in a given sequence.
"""
import unittest

def solution(A):
    # write your code in Python 2.7
    B = 100001 * [0]
    for i in range(len(A)):
        if A[i] > 0 and A[i] <= 100000:
            B[A[i]] = 1
    
    for i in range(1, 100001):
        if B[i] == 0:
            return i
    
    return 100001

class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution([1, 3, 1, 8, 2, 3, 5, 4]), 6)
        self.assertEqual(solution([3, 4, 3]), 1)
        self.assertEqual(solution([1, 2, 4, 3]), 5)
        
if __name__ == '__main__':
    unittest.main(exit=False)
