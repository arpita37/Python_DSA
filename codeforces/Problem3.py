import sys
T = int(input())

while(T):
    N = int(input())
    arr = list(map(int,input().strip().split()))
    ans = min(arr[0],arr[1])
    for i in range(1,N-1):
        temp = [0,0,0]
        temp[0] = arr[i-1]
        temp[1] = arr[i]
        temp[2] = arr[i+1]
        temp.sort()
        ans = max(ans,temp[1])
    print(ans)
    T -= 1