'''https://www.geeksforgeeks.org/problems/shortest-job-first/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=shortest-job-first'''
#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def solve(self, bt):
        # Code here
        bt.sort()
        wt_time = total = 0
        for i in range(len(bt)):
            total += wt_time
            wt_time += bt[i]
        
        return total//len(bt)
            

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        bt = list(map(int, input().split()))
        ob = Solution()
        res = ob.solve(bt)
        print(res)
# } Driver Code Ends