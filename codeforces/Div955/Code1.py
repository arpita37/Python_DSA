T = int(input())
while(T):
    x1,y1 = list(map(int,input().strip().split()))
    x2,y2 = list(map(int,input().strip().split()))
    if x1 == x2 and y1 == y2:
        print("YES")
    elif x1 != x2 and y1 != y2:
        # do something
        if x1 < y1:
            if x2<y2:
                print("YES")
            else:
                print("NO")
        
        if x1 > y1:
            if x2 > y2:
                print("YES")
            else:
                print("NO")
    elif x1 == x2 and y1 != y2:
        if x1 <= y1 or x1 >= y2:
            print("YES")
        else:
            print("NO")
    elif x1 != x2 and y1 == y2:
        if y1 <= x1 or y1 >= x2:
            print( "YES")
        else:
            print("NO")

    T -= 1