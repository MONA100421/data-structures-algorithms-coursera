
# Same interface as preprocess_large; we still use bidirectional Dijkstra.
import sys, heapq
sys.setrecursionlimit(10**7)

def bidir_dijkstra(n, adj, rev, s, t):
    if s==t: return 0
    INF=10**18
    distF=[INF]*n; distB=[INF]*n
    procF=[False]*n; procB=[False]*n
    distF[s]=0; distB[t]=0
    qF=[(0,s)]; qB=[(0,t)]
    best=INF
    while qF or qB:
        if qF:
            d,u=heapq.heappop(qF)
            if d==distF[u]:
                procF[u]=True
                if procB[u]: best=min(best, distF[u]+distB[u])
                for v,w in adj[u]:
                    nd=d+w
                    if nd<distF[v]:
                        distF[v]=nd; heapq.heappush(qF,(nd,v))
        if qB:
            d,u=heapq.heappop(qB)
            if d==distB[u]:
                procB[u]=True
                if procF[u]: best=min(best, distF[u]+distB[u])
                for v,w in rev[u]:
                    nd=d+w
                    if nd<distB[v]:
                        distB[v]=nd; heapq.heappush(qB,(nd,v))
        if best<10**18:
            # stop if min remaining distances can't beat best
            minF = qF[0][0] if qF else 10**18
            minB = qB[0][0] if qB else 10**18
            if minF + minB >= best:
                break
    return -1 if best==INF else best

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(map(int,data))
    n=next(it); m=next(it)
    adj=[[] for _ in range(n)]; rev=[[] for _ in range(n)]
    for _ in range(m):
        u=next(it)-1; v=next(it)-1; w=next(it)
        adj[u].append((v,w)); rev[v].append((u,w))
    print("Ready")
    q=next(it)
    out=[]
    for _ in range(q):
        s=next(it)-1; t=next(it)-1
        out.append(str(bidir_dijkstra(n,adj,rev,s,t)))
    sys.stdout.write("\n".join(out))

if __name__=="__main__":
    main()
