def find(idx,n):
    if idx >= n//2:
        return True
    if arr[idx] != arr[n-idx-1]:
        return False
    return find(idx+1,n)


arr = list(map(int,input().strip().split()))
print( find(0,len(arr)) )