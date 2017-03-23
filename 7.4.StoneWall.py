"""
7.4.StoneWall
Cover "Manhattan skyline" using the minimum number of rectangles.
"""
import unittest

def solution(H):
    # write your code in Python 2.7
    stack = [0]
    n = 0
    for h in H:
        # print "1 ", stack
        while len(stack) > 0:
            prev = stack.pop()
                    
            if prev > h:
                n = n + 1
            elif prev == h:
                stack.append(h)
                break
            else:
                stack.append(prev)
                stack.append(h)
                break  
    
    return n + len(stack) - 1

class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution([8, 8]), 1)
        self.assertEqual(solution([8, 8, 5, 7, 9, 8, 7, 4, 8]), 7)
        
if __name__ == '__main__':
    unittest.main(exit=False)
