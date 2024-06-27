def recur(i):
    if i < 0:
        return 
    recur(i-1)
    print(i)

n = int(input())
recur(n)