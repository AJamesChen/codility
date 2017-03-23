"""
8.1.EquiLeader
Find the index S such that the leaders of the sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N - 1] are the same.
"""

import unittest

def solution(A):
    # write your code in Python 2.7
    if len(A) == 1:
        return 0
    
    D = {}
    
    leadKey = 1
    leadCount = 0
    
    for a in A:
        if a in D:
            D[a] = D[a] + 1
        else:
            D[a] = 1
    
        if leadCount < D[a]:
            leadCount = D[a]
            leadKey = a
    
    if leadCount < len(A) // 2:
        return 0
    
    count = 0
    s = 0
    
    for i in range(len(A)):
        if A[i] == leadKey:
            count = count + 1
        
        if count > (i + 1) // 2 and (leadCount -count) > (len(A) - i - 1) // 2:
            s = s + 1
    
    return s
        
class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution([8, 8]), 1)
        self.assertEqual(solution([4, 3, 4, 4, 4, 2]), 2)
        
if __name__ == '__main__':
    unittest.main(exit=False)
