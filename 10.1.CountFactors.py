"""
10.1.CountFactors
Count factors of given number n.
"""

import unittest

def solution(N):
    # write your code in Python 2.7
    i = 1
    total = 0
    
    while i * i <= N:
        if N % i == 0:
            total = total + 2
        i = i + 1
    
    i = i - 1
    if i * i == N:
        total = total - 1
    
    return total
        
class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution(1), 1)
        self.assertEqual(solution(16), 5)
        self.assertEqual(solution(36), 9)
        self.assertEqual(solution(24), 8)
        
if __name__ == '__main__':
    unittest.main(exit=False)
