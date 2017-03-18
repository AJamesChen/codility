"""
5.3.GenomicRangeQuery
Find the minimal nucleotide from a range of sequence DNA.
"""
import unittest

def solution(S, P, Q):
    # write your code in Python 2.7
    LenS = len(S)
    
    PreSumA = (LenS + 1) * [0]
    PreSumC = (LenS + 1) * [0]
    PreSumG = (LenS + 1) * [0]
    PreSumT = (LenS + 1)* [0]
    
    SA = 0
    SC = 0
    SG = 0
    ST = 0
    
    for i in range(LenS):
        
        PreSumA[i] = SA
        PreSumC[i] = SC
        PreSumG[i] = SG
        PreSumT[i] = ST
    
        if S[i] == 'A':
            SA = SA + 1
        elif S[i] == 'C':
            SC = SC + 1
        elif S[i] == 'G':
            SG = SG + 1
        else:
            ST = ST + 1
        
    PreSumA[LenS] = SA
    PreSumC[LenS] = SC
    PreSumG[LenS] = SG
    PreSumT[LenS] = ST
    
    R = []
    LenPQ = len(P)
    
    for i in range(LenPQ):
        if PreSumA[P[i]] < PreSumA[Q[i] + 1]:
            R.append(1)
        elif PreSumC[P[i]] < PreSumC[Q[i] + 1]:
            R.append(2)
        elif PreSumG[P[i]] < PreSumG[Q[i] + 1]:
            R.append(3)
        else:
            R.append(4)
            
    return R

    
class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution('A', [0], [0]), [1])
        self.assertEqual(solution('AC', [0, 0, 1], [0, 1, 1]),  [1, 1, 2])
        self.assertEqual(solution('CAGCCTA', [2, 5, 0], [4, 5, 6]), [2, 4, 1])
        
if __name__ == '__main__':
    unittest.main(exit=False)

