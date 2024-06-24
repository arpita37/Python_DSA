from collections import defaultdict,deque
def bfs(s,adj,dist):
    q = deque()
    q.append(s)
    dist[s] = 1
    while(q):
        node = q.popleft()
        for nn in adj[node]:
            if dist[nn] == -1:
                dist[nn] = dist[node]+1
                q.append(nn)
    return dist

T = int(input())
while(T):
    N = int(input())
    [a,b] = list(map(int,input().strip().split()))
    a -= 1
    b -= 1
    adj = defaultdict(list)
    for e in range(N-1):
        [x,y] = list(map(int,input().strip().split()))
        x -= 1
        y -= 1
        adj[x].append(y)
        adj[y].append(x)
    dist_a = [-1]*N
    dist_b = [-1]*N
    dist_a = bfs(a,adj,dist_a)
    dist_b = bfs(b,adj,dist_b)
    maxdist = 0
    for i in range(N):
        if dist_b[i] > dist_a[i]:
            maxdist = max(maxdist, dist_b[i])
    print(maxdist)
    T -= 1