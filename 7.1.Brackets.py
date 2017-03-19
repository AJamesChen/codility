"""
7.1.Brackets
Determine whether a given string of parentheses is properly nested.
"""
import unittest

def solution(S):
    # write your code in Python 2.7
    stack = []
    
    for s in S:
        if s == '{' or s == '[' or s == '(':
            stack.append(s)
        else:
            if len(stack) == 0:
                return 0
                
            l = stack.pop()
            if s == '}' and l != '{':
                return 0
            elif s == ']' and l != '[':
                return 0
            elif s == ')' and l != '(':
                return 0
            
    
    if len(stack) == 0:
        return 1
    else:
        return 0

class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution("{[()()]}"),  1)
        self.assertEqual(solution("([)()]"),  0)
        
if __name__ == '__main__':
    unittest.main(exit=False)
