# use python3
import sys
from collections import defaultdict

def build_debruijn(reads, k):
    g = defaultdict(list)
    for r in reads:
        for i in range(len(r) - k + 1):
            g[r[i:i+k-1]].append(r[i+1:i+k])
    return g

def eulerian_path(g):
    stack, path = [], []
    u = next(iter(g))
    stack.append(u)
    while stack:
        u = stack[-1]
        if g[u]:
            v = g[u].pop()
            stack.append(v)
        else:
            path.append(stack.pop())
    return path[::-1]

if __name__ == "__main__":
    data = [line.strip() for line in sys.stdin if line.strip()]
    k = int(data[-1])
    reads = data[:-1]
    g = build_debruijn(reads, k)
    path = eulerian_path(g)
    genome = path[0] + "".join(p[-1] for p in path[1:])
    print(genome)
