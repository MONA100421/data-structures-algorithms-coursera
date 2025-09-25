# Uses python3
import sys

def negative_cycle(adj, cost):
    n = len(adj)
    INF = 10**18

    # Super source trick: initialize distances to 0
    dist = [0] * n

    edges = []
    for u in range(n):
        for i, v in enumerate(adj[u]):
            edges.append((u, v, cost[u][i]))

    # n-1 rounds
    for _ in range(n - 1):
        changed = False
        for u, v, w in edges:
            if dist[v] > dist[u] + w:
                dist[v] = max(-INF, dist[u] + w)
                changed = True
        if not changed:
            break

    # one more relaxation
    for u, v, w in edges:
        if dist[v] > dist[u] + w:
            return 1
    return 0

if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    n, m = data[0], data[1]
    ptr = 2
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for _ in range(m):
        a, b, w = data[ptr], data[ptr + 1], data[ptr + 2]
        ptr += 3
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
