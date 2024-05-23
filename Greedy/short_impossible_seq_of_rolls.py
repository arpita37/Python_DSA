'''https://leetcode.com/problems/shortest-impossible-sequence-of-rolls/'''

class obj:
    def __init__(self):
        self.li = []
        self.index = 0

class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        l = len(rolls)
        freq = defaultdict(obj)
        for i in range(l):
            freq[rolls[i]].li.append(i)
            
        max_len = 0
        for key,val in freq.items():
            max_len = max(max_len,len(val.li))
        
        prev = iterations = 0
        while(True):
            curr = 0
            iterations += 1
            for j in range(1,k+1):
                idx = freq[j].index
                while(idx<len(freq[j].li) and freq[j].li[idx] < prev):
                    idx += 1
                if idx == len(freq[j].li): 
                    return iterations
                freq[j].index = idx+1
                curr = max(freq[j].li[idx],curr)
            prev = curr
            
        return iterations
                
                    
                
                
            
            