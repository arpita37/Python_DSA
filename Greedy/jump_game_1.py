'''https://leetcode.com/problems/jump-game/submissions/'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_val = 0
        for i in range(n):
            if i > max_val:
                return False
            max_val = max(max_val,i+nums[i])
        return True