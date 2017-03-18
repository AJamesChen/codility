"""
6.3.Triangle
Determine whether a triangle can be built from a given set of edges.
"""
import unittest

def solution(A):
    # write your code in Python 2.7
    if len(A) < 3:
        return 0
        
    A.sort()
    
    for i in range(len(A) - 2):
        if A[i] + A[i + 1] > A[i + 2]:
            return 1
    
    return 0

class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution([10, 2, 5, 1, 8, 20]),  1)
        self.assertEqual(solution([10, 50, 5, 1]),  0)
        
if __name__ == '__main__':
    unittest.main(exit=False)
