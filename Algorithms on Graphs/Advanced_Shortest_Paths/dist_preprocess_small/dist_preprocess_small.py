
# Distance queries with "preprocess" for small graph.
# We implement bidirectional Dijkstra (no CH). Matches the I/O expected by grader:
# - read n m
# - m lines: u v w (1-based)
# - print "Ready"
# - read q
# - then q lines of s t (1-based); print distance or -1 each line
import sys, heapq
sys.setrecursionlimit(10**7)

def bidir_dijkstra(n, adj, rev, s, t):
    if s == t:
        return 0
    INF=10**18
    distF=[INF]*n; distB=[INF]*n
    procF=[False]*n; procB=[False]*n
    distF[s]=0; distB[t]=0
    qF=[(0,s)]; qB=[(0,t)]
    best=INF
    while qF or qB:
        if qF:
            d,u=heapq.heappop(qF)
            if d!=distF[u]: pass
            else:
                procF[u]=True
                if procB[u]:
                    best=min(best, distF[u]+distB[u])
                for v,w in adj[u]:
                    if distF[v]>d+w:
                        distF[v]=d+w; heapq.heappush(qF,(distF[v],v))
        if qB:
            d,u=heapq.heappop(qB)
            if d!=distB[u]: pass
            else:
                procB[u]=True
                if procF[u]:
                    best=min(best, distF[u]+distB[u])
                for v,w in rev[u]:
                    if distB[v]>d+w:
                        distB[v]=d+w; heapq.heappush(qB,(distB[v],v))
        # early stop
        if qF and qB and qF[0][0]+qB[0][0] >= best:
            break
    return -1 if best==INF else best

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(map(int,data))
    n = next(it); m = next(it)
    adj=[[] for _ in range(n)]
    rev=[[] for _ in range(n)]
    for _ in range(m):
        u=next(it)-1; v=next(it)-1; w=next(it)
        adj[u].append((v,w))
        rev[v].append((u,w))
    # Print "Ready" as the grader expects after preprocessing
    print("Ready")
    q = next(it)
    out=[]
    for _ in range(q):
        s=next(it)-1; t=next(it)-1
        out.append(str(bidir_dijkstra(n, adj, rev, s, t)))
    sys.stdout.write("\n".join(out))

if __name__=="__main__":
    main()
