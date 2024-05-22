'''https://leetcode.com/problems/split-a-string-in-balanced-strings/'''

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        c = 0
        for i in s:
            if i == "R":
                c += 1
            if i == "L":
                c -= 1
            if c == 0:
                count += 1
                
        return count