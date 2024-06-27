def recur(i,s):
    if i < 1:
        print(s)
        return
    recur(i-1,s+i)


n = int(input())
recur(n,0)
    