# use python3
from collections import deque

def circulation(n, edges):
    m = len(edges)
    lower_bounds = [l for (_, _, l, _) in edges]
    capacity = [c for (_, _, _, c) in edges]

    # 建立調整後的網路
    graph = [[] for _ in range(n + 2)]
    s, t = 0, n + 1
    balance = [0] * (n + 1)

    for i, (u, v, l, c) in enumerate(edges):
        balance[u] -= l
        balance[v] += l
        add_edge(graph, u, v, c - l, i)

    for v in range(1, n + 1):
        if balance[v] > 0:
            add_edge(graph, s, v, balance[v])
        elif balance[v] < 0:
            add_edge(graph, v, t, -balance[v])

    flow = max_flow(graph, s, t)
    if flow != sum(max(0, b) for b in balance):
        return None

    res = [0] * m
    for u in range(1, n + 1):
        for v, cap, rev, idx in graph[u]:
            if idx != -1:
                used = capacity[idx] - cap
                res[idx] = used
    return res

def add_edge(graph, u, v, cap, idx=-1):
    graph[u].append([v, cap, len(graph[v]), idx])
    graph[v].append([u, 0, len(graph[u]) - 1, -1])

def max_flow(graph, s, t):
    flow = 0
    INF = 10**9
    n = len(graph)
    while True:
        level = [-1] * n
        q = deque([s])
        level[s] = 0
        while q:
            u = q.popleft()
            for v, cap, _, _ in graph[u]:
                if cap > 0 and level[v] < 0:
                    level[v] = level[u] + 1
                    q.append(v)
        if level[t] < 0:
            return flow
        it = [0] * n
        f = dfs_flow(graph, s, t, INF, it, level)
        while f:
            flow += f
            f = dfs_flow(graph, s, t, INF, it, level)

def dfs_flow(graph, u, t, f, it, level):
    if u == t:
        return f
    for i in range(it[u], len(graph[u])):
        it[u] = i
        v, cap, rev, idx = graph[u][i]
        if cap > 0 and level[u] < level[v]:
            d = dfs_flow(graph, v, t, min(f, cap), it, level)
            if d > 0:
                graph[u][i][1] -= d
                graph[v][rev][1] += d
                return d
    return 0

if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    result = circulation(n, edges)
    if result is None:
        print("NO")
    else:
        print("YES")
        for f in result:
            print(f)
