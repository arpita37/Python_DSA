'''https://leetcode.com/problems/valid-parenthesis-string/'''
class Solution:
    def checkValidString(self, s: str) -> bool:
        braces = []
        stars = []
        for i,sym in enumerate(s):
            if sym == '(':
                braces.append(i)
            elif sym == '*':
                stars.append(i)
            else:
                if braces:
                    braces.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
        while braces and stars:
            if braces.pop() > stars.pop(): return False
        
        return len(braces) == 0