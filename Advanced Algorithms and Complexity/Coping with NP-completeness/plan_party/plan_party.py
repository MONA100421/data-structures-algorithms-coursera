# python3
import sys
sys.setrecursionlimit(10**7)

def read_input():
    n=int(sys.stdin.readline())
    weights=list(map(int,sys.stdin.readline().split()))
    edges=[[] for _ in range(n)]
    for _ in range(n-1):
        u,v=map(int,sys.stdin.readline().split())
        edges[u-1].append(v-1)
        edges[v-1].append(u-1)
    return n,weights,edges

def main():
    n,weights,edges=read_input()
    dp=[[0,0] for _ in range(n)]
    parent=[-1]*n
    order=[]
    stack=[0]
    while stack:
        u=stack.pop()
        order.append(u)
        for v in edges[u]:
            if v!=parent[u]:
                parent[v]=u
                stack.append(v)
    for u in reversed(order):
        dp[u][0]=0
        dp[u][1]=weights[u]
        for v in edges[u]:
            if v==parent[u]: continue
            dp[u][0]+=max(dp[v][0],dp[v][1])
            dp[u][1]+=dp[v][0]
    print(max(dp[0][0],dp[0][1]))

if __name__=="__main__":
    main()
