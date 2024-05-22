'''https://www.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1'''

#User function Template for python3

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, w,arr,n):
        
        # code here
        value_per_weight = [arr[i].value/arr[i].weight for i in range(n)]
        aux = [(arr[i].value,arr[i].weight,value_per_weight[i]) for i in range(n)]
        aux.sort(key = lambda x:x[2],reverse=True)
        ans = 0
        for i in range(n):
            if aux[i][1] <= w:
                ans += aux[i][0]
                w -= aux[i][1]
            else:
                ans += (aux[i][2]*w)
                w = 0
            if w == 0:break
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha


class Item:

    def __init__(self, val, w):
        self.value = val
        self.weight = w


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n, w = map(int, input().strip().split())
        info = list(map(int, input().strip().split()))
        arr = [Item(0, 0) for i in range(n)]
        for i in range(n):
            arr[i].value = info[2 * i]
            arr[i].weight = info[2 * i + 1]

        ob = Solution()
        print("%.6f" % ob.fractionalknapsack(w, arr, n))

# } Driver Code Ends