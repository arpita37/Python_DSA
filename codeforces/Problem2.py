import sys
from collections import Counter
T = int(input())

while(T):
    N = int(input())
    arr = list(map(int,input().strip().split()))
    arr.sort()
    if arr[0] == 1:
        print("Yes")
        T -= 1
        continue
    temp = [arr[0]]
    flag = True
    count1 = count2 = both = 0
    for i in range(N):
        if len(temp) == 1:
            if arr[i]%temp[0] != 0:
                temp.append(arr[i])
        elif len(temp) == 2:
            if arr[i]%temp[0] == 0 and arr[i]%temp[1] == 0:
                both += 1
            elif arr[i]%temp[0] == 0:
                count1 += 1
            elif arr[i]%temp[1] == 0:
                count2 += 1
            else:
                flag = False
                break
    if flag:
        if len(temp) <= 2:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
    T -= 1