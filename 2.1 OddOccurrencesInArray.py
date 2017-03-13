"""
2.1. OddOccurrencesInArray
Find value that occurs in odd number of elements.
"""

import unittest

def solution(A):
    # write your code in Python 2.7
    res = 0
    for a in A:
        res = a ^ res
    return res

class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution([9, 3, 9, 3, 9, 7, 9]), 7)
        self.assertEqual(solution([1]), 1)
                
if __name__ == '__main__':
    unittest.main(exit=False)
