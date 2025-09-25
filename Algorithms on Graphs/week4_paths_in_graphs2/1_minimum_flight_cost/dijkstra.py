# Uses python3
import sys

def negative_cycle(adj, cost):
    n = len(adj)
    INF = 10**18

    # super source: initialize all distances to 0
    dist = [0] * n

    # flatten edges
    edges = []
    for u in range(n):
        for i, v in enumerate(adj[u]):
            edges.append((u, v, cost[u][i]))

    # n-1 relaxations
    for _ in range(n - 1):
        changed = False
        for u, v, w in edges:
            if dist[v] > dist[u] + w:
                dist[v] = max(-INF, dist[u] + w)
                changed = True
        if not changed:
            break

    # one more pass: if anything can still be relaxed -> negative cycle exists
    for u, v, w in edges:
        if dist[v] > dist[u] + w:
            return 1
    return 0

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
    print(negative_cycle(adj, cost))
