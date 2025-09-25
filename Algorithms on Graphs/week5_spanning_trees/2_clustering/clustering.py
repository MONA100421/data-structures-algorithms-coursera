# Uses python3
import sys
import math

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        if self.rank[a] < self.rank[b]:
            a, b = b, a
        self.parent[b] = a
        if self.rank[a] == self.rank[b]:
            self.rank[a] += 1
        return True


def clustering(x, y, k):
    n = len(x)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            w = math.hypot(x[i] - x[j], y[i] - y[j])
            edges.append((w, i, j))
    edges.sort(key=lambda e: e[0])

    dsu = DSU(n)
    clusters = n

    for w, u, v in edges:
        if dsu.find(u) != dsu.find(v):
            if clusters == k:
                return w
            dsu.union(u, v)
            clusters -= 1

    return 0.0


if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
