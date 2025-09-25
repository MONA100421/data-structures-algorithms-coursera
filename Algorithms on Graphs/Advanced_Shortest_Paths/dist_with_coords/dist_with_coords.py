
# A* search on a directed graph with coordinates
import sys, math, heapq
sys.setrecursionlimit(10**7)

def astar(n, adj, cost, x, y, s, t):
    # zero-based s,t
    if s == t:
        return 0
    # Potential: straight-line distance to t
    def h(u):
        dx = x[u]-x[t]; dy = y[u]-y[t]
        return math.hypot(dx,dy)
    INF = 10**18
    dist = [INF]*n
    visited = [False]*n
    pq = []
    dist[s] = 0
    heapq.heappush(pq,(h(s), s))
    while pq:
        _, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True
        if u == t:
            return dist[u]
        du = dist[u]
        for i,v in enumerate(adj[u]):
            w = cost[u][i]
            if dist[v] > du + w:
                dist[v] = du + w
                heapq.heappush(pq, (dist[v] + h(v), v))
    return -1

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(map(int, data))
    n = next(it); m = next(it)
    x = [0]*n; y=[0]*n
    for i in range(n):
        x[i]=next(it); y[i]=next(it)
    adj=[[] for _ in range(n)]; cost=[[] for _ in range(n)]
    for _ in range(m):
        u=next(it)-1; v=next(it)-1; w=next(it)
        adj[u].append(v); cost[u].append(w)
    q = next(it)
    out=[]
    for _ in range(q):
        s=next(it)-1; t=next(it)-1
        out.append(str(astar(n,adj,cost,x,y,s,t)))
    sys.stdout.write("\n".join(out))

if __name__=="__main__":
    main()
