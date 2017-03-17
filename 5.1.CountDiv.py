"""
5.1.CountDiv
Compute number of integers divisible by k in range [a..b].
"""
import unittest

def solution(A, B, K):
    # write your code in Python 2.7
    R1 = A // K
    R2 = B // K
    
    if A % K == 0:
        return R2 - R1 + 1
    else:
        return R2 - R1
    
class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution(6, 11, 2),  3)
        
if __name__ == '__main__':
    unittest.main(exit=False)
