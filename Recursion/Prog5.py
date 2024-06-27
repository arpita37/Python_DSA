def recur(i):
    if i <= 1:
        return i
    return i + recur(i-1)


n = int(input())
print( recur(n) )
    