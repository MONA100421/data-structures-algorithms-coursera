# Uses python3
import sys
from collections import deque

def shortet_paths(adj, cost, s, distance, reachable, shortest):
    n = len(adj)
    INF = 10**18

    # 1) reachability from s
    q = deque([s])
    reachable[s] = 1
    while q:
        u = q.popleft()
        for v in adj[u]:
            if not reachable[v]:
                reachable[v] = 1
                q.append(v)

    # 2) Bellman–Ford on reachable subgraph
    distance[s] = 0
    edges = []
    for u in range(n):
        for i, v in enumerate(adj[u]):
            edges.append((u, v, cost[u][i]))

    for _ in range(n - 1):
        changed = False
        for u, v, w in edges:
            if reachable[u] and distance[u] != INF and distance[v] > distance[u] + w:
                distance[v] = distance[u] + w
                changed = True
        if not changed:
            break

    # 3) find vertices affected by (or reachable from) a negative cycle
    affected = [0] * n
    for u, v, w in edges:
        if reachable[u] and distance[u] != INF and distance[v] > distance[u] + w:
            affected[v] = 1

    dq = deque()
    visited = [False] * n
    for i in range(n):
        if affected[i]:
            dq.append(i)
            visited[i] = True
            shortest[i] = 0

    while dq:
        u = dq.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                shortest[v] = 0
                dq.append(v)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s = data[0] - 1
    distance = [10**19] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])
