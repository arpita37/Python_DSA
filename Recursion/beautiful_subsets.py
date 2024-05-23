'''https://leetcode.com/problems/the-number-of-beautiful-subsets/'''

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        self.ans = 0
        self.maxval = max(nums)+1
        
        def subsets(idx,curr):
            if idx == len(nums):
                return 
            #not pick
            subsets(idx+1,curr)
            #pick
            f1 = f2 = False
            if nums[idx]-k >= 0:
                if curr[nums[idx]-k] == 0:
                    f1 = True
            else:
                f1 = True
            if nums[idx]+k < self.maxval:
                if curr[nums[idx]+k] == 0:
                    f2 = True
            else:
                f2 = True
            if f1 and f2:
                curr[nums[idx]] += 1
                self.ans += 1
                subsets(idx+1,curr)
                curr[nums[idx]] -= 1
        
        subsets(0,[0]*self.maxval)
        return self.ans