arr = [9,3,2,9,3,4,2,3,7,4,9,4,2]
'''1001
1001
1001
0011
0011
0011
0011
0100
0100
0100
0010
0010
0010
0111'''

aux = [0]*32
def findsetbits(num):
    idx = 0
    while(num):
        v = num%2
        aux[idx] += v
        num //= 2
        idx += 1

for element in arr:
    findsetbits(element)
ans = 0

for i in range(32):
    v = aux[i]%3
    ans += v*(2**i)
print(ans)
