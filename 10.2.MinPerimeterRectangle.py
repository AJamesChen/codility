"""
10.2.MinPerimeterRectangle
Find the minimal perimeter of any rectangle whose area equals N.
"""

import unittest

def solution(N):
    # write your code in Python 2.7
    i = 1
    A = 1
    
    while i * i <= N:
        if N % i == 0:
            A = i
        i = i + 1
        
    return 2 * (A + N / A)
        
class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution(1), 4)
        self.assertEqual(solution(16), 16)
        self.assertEqual(solution(30), 22)
        self.assertEqual(solution(2), 6)
        
if __name__ == '__main__':
    unittest.main(exit=False)
