#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, math, heapq

INF = 10**18

def astar(n, coords, adj, s, t):
    if s == t:
        return 0
    # heuristic: straight-line distance
    def h(u):
        x1, y1 = coords[u]
        x2, y2 = coords[t]
        return math.hypot(x1 - x2, y1 - y2)

    dist = [INF] * n
    used = [False] * n
    dist[s] = 0
    pq = [(h(s), s)]  # (f = g + h, node)

    while pq:
        f, u = heapq.heappop(pq)
        if used[u]:
            continue
        used[u] = True
        if u == t:
            return dist[u]
        for v, w in adj[u]:
            nd = dist[u] + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd + h(v), v))
    return -1

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it))
    coords = []
    for _ in range(n):
        x = float(next(it)); y = float(next(it))
        coords.append((x, y))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        if 0 <= u < n and 0 <= v < n:
            adj[u].append((v, w))
    q = int(next(it))
    out = []
    for _ in range(q):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        ans = astar(n, coords, adj, s, t)
        out.append(str(ans if ans != -1 and ans < INF // 2 else -1))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
