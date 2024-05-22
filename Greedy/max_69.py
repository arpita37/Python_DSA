'''https://leetcode.com/problems/maximum-69-number/'''
class Solution:
    def maximum69Number (self, num: int) -> int:
        aux = [i for i in str(num)]
        for i in range(len(aux)):
            if aux[i] == '6':
                aux[i] = '9'
                break
        return int(''.join(aux))