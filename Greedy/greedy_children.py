'''https://leetcode.com/problems/assign-cookies/submissions/'''
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        i = j = count = 0
        while(i<len(g) and j < len(s)):
            while(j<len(s) and s[j] < g[i]):
                j += 1
            if j<len(s) and s[j] >= g[i]:
                count += 1
            i += 1
            j += 1
        return count