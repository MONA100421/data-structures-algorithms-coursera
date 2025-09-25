#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, heapq

INF = 10**18

def bidir_dijkstra(n, adj, radj, s, t):
    if s == t:
        return 0
    dist_f = [INF] * n
    dist_b = [INF] * n
    vis_f = [False] * n
    vis_b = [False] * n
    pqf, pqb = [], []
    dist_f[s] = 0
    dist_b[t] = 0
    heapq.heappush(pqf, (0, s))
    heapq.heappush(pqb, (0, t))
    best = INF

    while pqf or pqb:
        if pqf:
            df, u = heapq.heappop(pqf)
            if df == dist_f[u] and not vis_f[u]:
                vis_f[u] = True
                if vis_b[u]:
                    best = min(best, dist_f[u] + dist_b[u])
                for v, w in adj[u]:
                    nd = df + w
                    if nd < dist_f[v]:
                        dist_f[v] = nd
                        heapq.heappush(pqf, (nd, v))

        if pqb:
            db, u = heapq.heappop(pqb)
            if db == dist_b[u] and not vis_b[u]:
                vis_b[u] = True
                if vis_f[u]:
                    best = min(best, dist_f[u] + dist_b[u])
                for v, w in radj[u]:
                    nd = db + w
                    if nd < dist_b[v]:
                        dist_b[v] = nd
                        heapq.heappush(pqb, (nd, v))

        if pqf and pqb and best < INF and pqf[0][0] + pqb[0][0] >= best:
            break

    return -1 if best >= INF else best

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it))
    adj = [[] for _ in range(n)]
    radj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        if 0 <= u < n and 0 <= v < n:
            adj[u].append((v, w))
            radj[v].append((u, w))

    sys.stdout.write("Ready\n")
    sys.stdout.flush()

    out = []
    try:
        q = int(next(it))
    except StopIteration:
        q = 0
    for _ in range(q):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        out.append(str(bidir_dijkstra(n, adj, radj, s, t)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
