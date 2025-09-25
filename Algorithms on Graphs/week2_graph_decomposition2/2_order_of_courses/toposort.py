# Uses python3
import sys
sys.setrecursionlimit(10**7)

def dfs(adj, used, order, x):
    used[x] = True
    for y in adj[x]:
        if not used[y]:
            dfs(adj, used, order, y)
    # post-order push
    order.append(x)

def toposort(adj):
    n = len(adj)
    used = [False] * n
    order = []
    for v in range(n):
        if not used[v]:
            dfs(adj, used, order, v)
    order.reverse()
    return order

if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    n, m = data[0], data[1]
    edges = list(zip(data[2:2+2*m:2], data[3:2+2*m:2]))
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')
