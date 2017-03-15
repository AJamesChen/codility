"""
TapeEquilibrium
Minimize the value |(A[0] + ... + A[P-1]) - (A[P] + ... + A[N-1])|.
"""
import unittest

def solution(A):
    # write your code in Python 2.7
    N = len(A)
    B = N * [A[0]]
    
    for i in range(1, N):
        B[i] = B[i - 1] + A[i]
    
    for i in range(0, N -1):
        B[i] = abs(B[i] * 2 - B[N - 1])

    return min(B[ : N -1])

class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution([3, 1, 2, 4, 3]), 1)
        
if __name__ == '__main__':
    unittest.main(exit=False)

