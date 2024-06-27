def reverse(idx,n):
    if idx >= n//2:
        return
    arr[idx],arr[n-idx-1] = arr[n-idx-1],arr[idx]
    reverse(idx+1,n)


arr = list(map(int,input().strip().split()))
reverse(0,len(arr))
print(arr)