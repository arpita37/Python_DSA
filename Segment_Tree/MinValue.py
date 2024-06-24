import sys
class Segment_Tree: #aux is 1-based indexing, arr is 0-based indexing
    def __init__(self):
        self.aux = []
        self.arr = []
        self.l = 0

    def __buildTree(self,idx,s,e):
        #base case
        if s == e:
            self.aux[idx] = self.arr[e]
            return
        else:
            mid = s+(e-s)//2
            left = 2*idx
            right = 2*idx+1
            self.__buildTree(left,s,mid)
            self.__buildTree(right,mid+1,e)
            self.aux[idx] = min(self.aux[left],self.aux[right])

    def build(self,arr):
        self.arr = arr
        self.l = len(arr)
        self.aux = [0]*(4*self.l)
        self.__buildTree(1,0,self.l-1)

    def __query(self,idx,s,e,l,r):
        if e<l or s>r:
            return sys.maxsize
        if s==e or (l <= s and r >= e):
            return self.aux[idx]
        mid = s+(e-s)//2
        # left = right = sys.maxsize
        # if l <= mid:
        #     if r <= mid:
        #         left = 
        #     else:
        #         left = self.__query(idx*2,s,mid,l,mid)
        #         right = self.__query(idx*2+1,mid+1,e,mid+1,r)
        # else:
        #     if r < mid:
        #         return sys.maxsize
        #     else:
        #         right = self.__query(idx*2+1,mid+1,e,l,r)
        # return min(left,right)
        left = self.__query(idx*2,s,mid,l,mid)
        right = self.__query(idx*2+1,mid+1,e,l,r)
        return min(left,right)



    def query(self,l,r):
        ans = self.__query(1,0,self.l-1,l,r)
        return ans


arr = [8,7,4,2,5,3,1,10] 
T = Segment_Tree()
T.build(arr)
print(T.aux)
print(T.arr)
print(T.query(0,7))
print(T.query(3,7))
print(T.query(2,6))
print(T.query(0,1))

    
