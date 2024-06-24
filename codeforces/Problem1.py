import sys
T = int(input())

while(T):
    N = int(input())
    arr = list(map(int,input().strip().split()))
    prev_min = sys.maxsize
    count = idx = 0
    stk = []
    while(idx<N):
        temp = []
        while(idx+1<N and arr[idx+1]>=arr[idx]):
            temp.append(arr[idx])
            idx += 1
        temp.append(arr[idx])
        stk.append(temp)
        idx += 1
        count += 1
    if count <= 2:
        if count == 2:
            if stk[1][-1] <= stk[0][0]:
                print("Yes")
            else:
                print("No")
        else:
            print("Yes")
    else:
        print("No")
        
    T -= 1