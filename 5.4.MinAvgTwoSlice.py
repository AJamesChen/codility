"""
5.4.MinAvgTwoSlice
Find the minimal average of any slice containing at least two elements.
"""
import unittest

def solution(A):
    # write your code in Python 2.7
    PreSum = [A[0]]
    
    for i in range(1, len(A)):
        PreSum.append(PreSum[i - 1] + A[i])
    
    minAvg = 10000;   
    minStart = 0
    start = 0
    
    for i in range(1, len(PreSum)):
        avg = (PreSum[i] - PreSum[start] + A[start]) /float(i + 1 - start)
        
        if avg < minAvg:
            minAvg = avg
            minStart = start
            
        if A[i] < minAvg:
            start = i
               
    return minStart
    
class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution([4, 2, 2, 5, 1, 5, 8]),  1)
        
if __name__ == '__main__':
    unittest.main(exit=False)

