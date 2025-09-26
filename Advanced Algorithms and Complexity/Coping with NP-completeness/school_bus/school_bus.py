# python3
import sys

def read_input():
    n,m=map(int,sys.stdin.readline().split())
    INF=10**15
    dist=[[INF]*n for _ in range(n)]
    for i in range(n):
        dist[i][i]=0
    for _ in range(m):
        u,v,w=map(int,sys.stdin.readline().split())
        u-=1;v-=1
        dist[u][v]=min(dist[u][v],w)
        dist[v][u]=min(dist[v][u],w)
    return n,dist

def tsp(n,dist):
    INF=10**15
    dp=[[INF]*n for _ in range(1<<n)]
    parent=[[-1]*n for _ in range(1<<n)]
    dp[1][0]=0
    for mask in range(1<<n):
        for u in range(n):
            if dp[mask][u]<INF:
                for v in range(n):
                    if not (mask&(1<<v)) and dist[u][v]<INF:
                        newmask=mask| (1<<v)
                        if dp[newmask][v]>dp[mask][u]+dist[u][v]:
                            dp[newmask][v]=dp[mask][u]+dist[u][v]
                            parent[newmask][v]=u
    full=(1<<n)-1
    best=INF
    last=-1
    for u in range(n):
        if dp[full][u]+dist[u][0]<best:
            best=dp[full][u]+dist[u][0]
            last=u
    if best>=INF: return -1,[]
    path=[]
    mask=full
    while last!=-1:
        path.append(last+1)
        last,parent_mask=last,parent[mask][last]
        if parent_mask==-1: break
        mask^=(1<<path[-1]-1)
        last=parent_mask
    path.reverse()
    return best,path+[1]

def main():
    n,dist=read_input()
    best,path=tsp(n,dist)
    if best==-1:
        print(-1)
    else:
        print(best)
        print(" ".join(map(str,path)))

if __name__=="__main__":
    main()
