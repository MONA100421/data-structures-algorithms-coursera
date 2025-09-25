# Uses python3
import sys
sys.setrecursionlimit(10**7)

def number_of_strongly_connected_components(adj):
    n = len(adj)
    # build reverse graph
    radj = [[] for _ in range(n)]
    for u in range(n):
        for v in adj[u]:
            radj[v].append(u)

    # 1) order by reverse-graph postorder
    used = [False] * n
    order = []

    def dfs1(u):
        used[u] = True
        for v in radj[u]:
            if not used[v]:
                dfs1(v)
        order.append(u)

    for u in range(n):
        if not used[u]:
            dfs1(u)

    # 2) explore original graph in that order
    used = [False] * n

    def dfs2(u):
        used[u] = True
        for v in adj[u]:
            if not used[v]:
                dfs2(v)

    scc = 0
    for u in reversed(order):
        if not used[u]:
            scc += 1
            dfs2(u)

    return scc


if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    n, m = data[0], data[1]
    edges = list(zip(data[2:2+2*m:2], data[3:2+2*m:2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
