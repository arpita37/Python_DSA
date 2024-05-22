'''https://www.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1'''

#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        aux = []
        for i in range(n):
            aux.append((start[i],end[i],end[i]-start[i]))
            
        aux.sort(key = lambda x:(x[1],x[2]))
        i = count = curr = 0
        while(i<n):
            if aux[i][0] > curr:
                count += 1
                curr = aux[i][1]
            i += 1
        return count
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends