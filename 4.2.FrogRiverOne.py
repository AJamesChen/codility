"""
FrogRiverOne
Find the earliest time when a frog can jump to the other side of a river.
"""
import unittest

def solution(X, A):
    # write your code in Python 2.7
    L = len(A)
    if X > L:
        return -1
    
    S = set()
    Min = 1000001
    Max = 0
    
    for i in range(L):
        Min = min(Min, A[i])
        Max = max(Max, A[i])
        S.add(A[i])
        
        if Min == 1 and Max == X and len(S) == Max:
            return i
    
    return -1

class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]), 6)
        self.assertEqual(solution(2, [3, 1, 2, 4, 3]), -1)
        self.assertEqual(solution(3, [2, 4, 3]), -1)
        
if __name__ == '__main__':
    unittest.main(exit=False)
