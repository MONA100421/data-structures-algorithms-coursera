# use python3
import sys
from collections import defaultdict

def de_bruijn(k):
    alphabet = ["0", "1"]
    n = len(alphabet)
    edges = defaultdict(list)
    for i in range(n**(k-1)):
        prefix = format(i, '0{}b'.format(k-1))
        for c in alphabet:
            edges[prefix].append(prefix[1:]+c)
    start = format(0, '0{}b'.format(k-1))
    return edges, start

def eulerian_cycle(edges, start):
    stack = [start]
    path = []
    while stack:
        v = stack[-1]
        if edges[v]:
            stack.append(edges[v].pop())
        else:
            path.append(stack.pop())
    return path[::-1]

def main():
    k = int(sys.stdin.readline())
    edges, start = de_bruijn(k)
    cycle = eulerian_cycle(edges, start)
    res = cycle[0]
    for node in cycle[1:]:
        res += node[-1]
    print(res[:-(k-1)])

if __name__ == "__main__":
    main()
