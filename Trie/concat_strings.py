'''https://leetcode.com/problems/concatenated-words/'''

class Trie:
    def __init__(self):
        self.d = [{},0]
    
    def insert_word(self,word):
        node = self.d
        for i in word:
            if i not in node[0]:
                node[0][i] = [{},0]
            node = node[0][i]
        node[1] += 1
            
    def find_word(self,word,offset):
        node = self.d
        ans = list()
        for i in range(offset,len(word)):
            if word[i] in node[0]:
                node = node[0][word[i]]
                if node[1] > 0:
                    ans.append((offset,i))
            else:
                return ans
        return ans
        
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        aux = [(w,len(w)) for w in words]
        aux.sort(key = lambda x:x[1])
        ans = []
        
        r = Trie()
        for w,l in aux:
            r.insert_word(w)
                               
        for w,l in aux:
            curr = [-1]
            while len(curr) > 0:
                temp = []
                for v in curr:
                    if v == l:
                        flag = True
                        break
                    res = r.find_word(w,v+1)
                    temp.extend(res)
                if flag == True or temp == []:
                    break
                curr = temp
            if flag:
                ans.append(w)

        return ans

