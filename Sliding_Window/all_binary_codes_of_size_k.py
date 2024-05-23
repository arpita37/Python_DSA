'''https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/'''
from collections import deque
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        end = start = 0
        l = len(s)
        curr = deque()
        visited = set()
        while(end<l):
            curr.append(s[end])
            if end-start+1 == k:
                visited.add("".join(curr))
                curr.popleft()
                start += 1
            end += 1
        return len(visited) == pow(2,k)