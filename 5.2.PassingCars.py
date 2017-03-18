"""
5.2. PassingCars
Count the number of passing cars on the road.
"""
import unittest

def solution(A):
    # write your code in Python 2.7
    s = 0
    
    se = 0
    
    for a in A:
        if a == 0:
            se = se + 1
        else:
            s = s + se
            if s > 1000000000:
                return -1
    
    return s
    
class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution([0, 1, 0, 1, 1]),  5)
        
if __name__ == '__main__':
    unittest.main(exit=False)
