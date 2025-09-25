#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from collections import deque

def bidir_bfs(adj, s, t):
    if s == t:
        return 0
    n = len(adj)
    dist_f = [-1] * n
    dist_b = [-1] * n
    qf, qb = deque(), deque()

    dist_f[s] = 0
    dist_b[t] = 0
    qf.append(s)
    qb.append(t)

    while qf and qb:
        if len(qf) <= len(qb):
            for _ in range(len(qf)):
                u = qf.popleft()
                du = dist_f[u]
                for v in adj[u]:
                    if dist_f[v] == -1:
                        dist_f[v] = du + 1
                        if dist_b[v] != -1:
                            return dist_f[v] + dist_b[v]
                        qf.append(v)
        else:
            for _ in range(len(qb)):
                u = qb.popleft()
                du = dist_b[u]
                for v in adj[u]:
                    if dist_b[v] == -1:
                        dist_b[v] = du + 1
                        if dist_f[v] != -1:
                            return dist_f[v] + dist_b[v]
                        qb.append(v)
    return -1

def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    it = iter(data)
    n = next(it); m = next(it)
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        if 0 <= u < n and 0 <= v < n:
            adj[u].append(v)
            adj[v].append(u)
    out = []
    try:
        q = next(it)
    except StopIteration:
        q = 0
    for _ in range(q):
        s = next(it) - 1
        t = next(it) - 1
        out.append(str(bidir_bfs(adj, s, t)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
