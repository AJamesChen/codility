"""
4.4.MaxCounters
Calculate the values of counters after applying all alternating operations: increase counter by 1; set value of all counters to current maximum.
"""
import unittest

def solution(N, A):
    # write your code in Python 2.7
    B = N * [0]
    Max = 0
    Base = 0
    for a in A:
        if a >= 1 and a <= N:
            if B[a - 1] < Base:
                B[a - 1] = 1 + Base
            else:
                B[a -1] = B[a -1] + 1
            Max = max(Max, B[a - 1])
        elif a == (N + 1):
            Base = Max
            
    for i in range(N):
        if B[i] < Base:
            B[i] = Base
    
    return B

class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution(5, [3, 4, 4, 6, 1, 4, 4]),  [3, 2, 2, 4, 2])
        
if __name__ == '__main__':
    unittest.main(exit=False)
