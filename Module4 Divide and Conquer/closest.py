import math
import sys
sys.setrecursionlimit(10**7)

def dist2(a, b):
    dx, dy = a[0]-b[0], a[1]-b[1]
    return dx*dx + dy*dy

def brute(pts):
    m = float('inf')
    for i in range(len(pts)):
        for j in range(i+1, len(pts)):
            m = min(m, dist2(pts[i], pts[j]))
    return m

def strip_min(strip, d2):
    # strip points are sorted by y
    m = d2
    n = len(strip)
    for i in range(n):
        j = i + 1
        while j < n and (strip[j][1] - strip[i][1])**2 < m:
            m = min(m, dist2(strip[i], strip[j]))
            j += 1
    return m

def rec(px, py):
    n = len(px)
    if n <= 3:
        return brute(px)
    mid = n // 2
    midx = px[mid][0]
    Lx, Rx = px[:mid], px[mid:]

    Ly, Ry = [], []
    left_set = set(Lx)
    for p in py:
        (Ly if p in left_set else Ry).append(p)

    d2 = min(rec(Lx, Ly), rec(Rx, Ry))

    # create strip
    strip = [p for p in py if (p[0] - midx)**2 < d2]
    d2 = strip_min(strip, d2)
    return d2

if __name__ == '__main__':
    data = list(map(int, open(0).read().split()))
    n = data[0]
    pts = [(data[i], data[i+1]) for i in range(1, 2*n, 2)]
    px = sorted(pts)                 # by x then y
    py = sorted(pts, key=lambda p: p[1])  # by y
    ans2 = rec(px, py)
    print("{:.9f}".format(math.sqrt(ans2)))
