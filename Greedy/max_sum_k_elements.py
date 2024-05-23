'''https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/'''
class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        score = max(nums)
        for i in range(k-1):
            max_val += 1
            score += max_val
        return score