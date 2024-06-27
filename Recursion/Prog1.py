def recur(i,n):
    if i > n:
        return 
    print(i)
    recur(i+1,n)

n = int(input())
recur(1,n)
