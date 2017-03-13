"""
1. BinaryGap (https://codility.com/demo/results/trainingW3SKEC-XJW/)
Find longest sequence of zeros in binary representation of an integer.
"""
import unittest

def BinaryGap(N):
    # write your code in Python 2.7
    
    while (N != 0) and (N & 1 == 0):
        N = N >> 1
    
    gap = 0
    mgap = 0
    
    while N != 0:
        if N & 1 == 1:
            mgap = max(gap, mgap)
            gap = 0
        else:
            gap = gap + 1
        
        N = N >> 1
    
    return mgap

class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(BinaryGap(1041), 5)
        self.assertEqual(BinaryGap(15), 0)
        self.assertEqual(BinaryGap(2147483647), 0)
        self.assertEqual(BinaryGap(328), 2)
        self.assertEqual(BinaryGap(6), 0)
        self.assertEqual(BinaryGap(561892), 3)
        self.assertEqual(BinaryGap(1162), 3)
        self.assertEqual(BinaryGap(1073741825), 29)
        self.assertEqual(BinaryGap(1610612737), 28)
        
if __name__ == '__main__':
    unittest.main(exit=False)


