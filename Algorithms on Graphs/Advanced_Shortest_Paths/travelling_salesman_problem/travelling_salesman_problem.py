#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, math, time
from random import randint

def dist(p, q):
    return math.hypot(p[0] - q[0], p[1] - q[1])

def tour_length(order, pts):
    n = len(order)
    d = 0.0
    for i in range(n):
        a = order[i]
        b = order[(i + 1) % n]
        d += dist(pts[a], pts[b])
    return d

def nearest_neighbor(pts, start=0):
    n = len(pts)
    used = [False] * n
    order = [start]
    used[start] = True
    for _ in range(n - 1):
        last = order[-1]
        best = -1
        bestd = 1e100
        for v in range(n):
            if not used[v]:
                d = dist(pts[last], pts[v])
                if d < bestd:
                    bestd = d
                    best = v
        used[best] = True
        order.append(best)
    return order

def two_opt(order, pts, time_limit=1.5):
    n = len(order)
    if n <= 3:
        return order
    start_time = time.time()
    improved = True
    while improved and (time.time() - start_time) < time_limit:
        improved = False
        for i in range(n - 1):
            a = order[i]
            b = order[(i + 1) % n]
            for j in range(i + 2, n if i > 0 else n - 1):
                c = order[j]
                d = order[(j + 1) % n]
                dab = dist(pts[a], pts[b]) + dist(pts[c], pts[d])
                dcd = dist(pts[a], pts[c]) + dist(pts[b], pts[d])
                if dcd + 1e-12 < dab:
                    l, r = i + 1, j
                    while l < r:
                        order[l], order[r] = order[r], order[l]
                        l += 1; r -= 1
                    improved = True
                    if (time.time() - start_time) > time_limit:
                        break
            if improved and (time.time() - start_time) > time_limit:
                break
    return order

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    pts = [(float(next(it)), float(next(it))) for _ in range(n)]

    candidates = [0]
    if n > 30:
        for _ in range(4):
            candidates.append(randint(0, n - 1))

    best_order = None
    best_len = 1e100
    for s in candidates:
        order = nearest_neighbor(pts, s)
        order = two_opt(order, pts, time_limit=1.2)
        L = tour_length(order, pts)
        if L < best_len:
            best_len = L
            best_order = order

    sys.stdout.write("{:.9f}\n".format(best_len))
    sys.stdout.write(" ".join(map(str, best_order)) + "\n")

if __name__ == "__main__":
    main()
