'''https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/'''

class Solution:
    def minimumSum(self, num: int) -> int:
        aux = []
        while(num):
            aux.append(num%10)
            num //= 10
            
        aux.sort()
        ans = ( aux[0]*10+aux[3] ) + (aux[1]*10+aux[2])
        return ans
        