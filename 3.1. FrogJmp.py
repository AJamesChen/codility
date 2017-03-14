"""
1. FrogJmp
Count minimal number of jumps from position X to Y.
"""

import unittest

def solution(X, Y, D):
    # write your code in Python 2.7
    step = (Y - X) // D
    
    if (Y - X) % D != 0:
        step = step + 1 
    
    return step

class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution(10, 85, 30), 3)
        self.assertEqual(solution(10, 70, 20), 3)
if __name__ == '__main__':
    unittest.main(exit=False)
