"""
7.3.Nesting
Determine whether given string of parentheses is properly nested.
"""
import unittest

def solution(S):
    # write your code in Python 2.7
    stack = []
    
    for s in S:
        if s == '(':
            stack.append(s)
        elif s == ')':
            if len(stack) == 0:
                return 0
            else:
                stack.pop()
    
    if len(stack) == 0:
        return 1
    else:
        return 0

class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution( ""), 1)
        self.assertEqual(solution("UV"), 1)
        self.assertEqual(solution( "(U)"), 1)
        self.assertEqual(solution("(()(())())"), 1)
        self.assertEqual(solution("(()"), 0)
        self.assertEqual(solution("())"), 0)
        
if __name__ == '__main__':
    unittest.main(exit=False)
