# Simple heuristic TSP solver: nearest neighbor + 2-opt
import sys, math, random

def dist(p, q):
    return math.hypot(p[0]-q[0], p[1]-q[1])

def total_len(order, pts):
    s = 0.0
    n = len(order)
    for i in range(n):
        s += dist(pts[order[i]], pts[order[(i+1)%n]])
    return s

def two_opt(order, pts):
    n = len(order)
    improved = True
    while improved:
        improved = False
        for i in range(n-1):
            a, b = order[i], order[(i+1)%n]
            for j in range(i+2, n if i>0 else n-1):
                c, d = order[j], order[(j+1)%n]
                dab = dist(pts[a], pts[b])
                dcd = dist(pts[c], pts[d])
                dac = dist(pts[a], pts[c])
                dbd = dist(pts[b], pts[d])
                if dac + dbd + 1e-9 < dab + dcd:
                    # reverse segment (i+1..j)
                    order[i+1:j+1] = reversed(order[i+1:j+1])
                    improved = True
        # optional: break early for big n
    return order

def nearest_neighbor(pts):
    n = len(pts)
    used = [False]*n
    order = [0]
    used[0]=True
    for _ in range(n-1):
        last = order[-1]
        best = None; bestd = 1e100
        for i in range(n):
            if not used[i]:
                d = dist(pts[last], pts[i])
                if d < bestd:
                    bestd = d; best = i
        used[best] = True
        order.append(best)
    return order

def main():
    data = sys.stdin.read().strip().split()
    if not data: 
        return
    it = iter(map(float, data))
    n = int(next(it))
    pts = [(int(next(it)), int(next(it))) for _ in range(n)]
    order = nearest_neighbor(pts)
    order = two_opt(order, pts)
    length = total_len(order, pts)
    print("{:.9f}".format(length))
    print(" ".join(map(str, order)))
if __name__=="__main__":
    main()
