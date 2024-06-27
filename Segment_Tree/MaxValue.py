class NumArray: #aux is 1-based indexing, arr is 0-based indexing
    def __init__(self, nums: List[int]):
        self.aux = []
        self.arr = nums
        self.l = len(nums)
        self.aux = [0]*(4*self.l+1)
        self.__buildTree(1,0,self.l-1)

    def __buildTree(self,idx,s,e):
        #base case
        if s == e:
            self.aux[idx] = self.arr[e]
        else:
            mid = s+(e-s)//2
            self.__buildTree(2*idx,s,mid)
            self.__buildTree(2*idx+1,mid+1,e)
            self.aux[idx] = self.aux[left] + self.aux[right]
    
    def __update(self,idx,s,e,up_idx,val):
        if e<s:
            return
        if s == e:
            if s == up_idx:
                self.aux[idx] = val
            return
        mid = s+(e-s)//2
        left = self.aux[2*idx]
        right = self.aux[2*idx+1]
        if mid >= up_idx:
            self.__update(2*idx,s,mid,up_idx,val)
            left = self.aux[2*idx]
        else:
            self.__update(2*idx+1,mid+1,e,up_idx,val)
            right = self.aux[2*idx+1]
        self.aux[idx] = left+right
    
    def update(self, index: int, val: int) -> None:
        self.arr[index] = val
        self.__update(1,0,self.l-1,index,val)
        
    def __query(self,idx,s,e,l,r):
        if e<l or s>r:
            return 0
        if s==e or (l <= s and r >= e):
            return self.aux[idx]
        mid = s+(e-s)//2
        left = self.__query(idx*2,s,mid,l,r)
        right = self.__query(idx*2+1,mid+1,e,l,r)
        return left+right


    def sumRange(self, left: int, right: int) -> int:
        ans = self.__query(1,0,self.l-1,left,right)
        return ans
        