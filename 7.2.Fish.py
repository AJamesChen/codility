"""
7.2.Fish
N voracious fish are moving along a river. Calculate how many fish are alive.
"""
import unittest

def solution(A, B):
    # write your code in Python 2.7
    upstream = []
    s = 0
    
    for i in range(len(A)):
        if B[i] == 1:
            upstream.append(A[i])
        else:
            if len(upstream) == 0:
                s = s + 1
            elif len(upstream) != 0:
                while len(upstream) != 0:
                    u = upstream.pop()
                    if u > A[i]:
                        upstream.append(u)
                        break
                if len(upstream) == 0:
                    s = s + 1
        
    s = s + len(upstream)
    return s

class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]), 2)
        
if __name__ == '__main__':
    unittest.main(exit=False)
