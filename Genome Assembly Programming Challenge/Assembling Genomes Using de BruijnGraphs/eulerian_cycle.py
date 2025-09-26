# use python3
# import sys
from collections import defaultdict, deque

def read_input():
    n, m = map(int, sys.stdin.readline().split())
    edges = defaultdict(deque)
    indeg = [0]*(n+1)
    outdeg = [0]*(n+1)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges[u].append(v)
        outdeg[u]+=1
        indeg[v]+=1
    return n, m, edges, indeg, outdeg

def hierholzer(start, edges, m):
    stack = [start]
    path = []
    while stack:
        v = stack[-1]
        if edges[v]:
            stack.append(edges[v].popleft())
        else:
            path.append(stack.pop())
    return path[::-1]

def main():
    n, m, edges, indeg, outdeg = read_input()
    for i in range(1, n+1):
        if indeg[i] != outdeg[i]:
            print(0)
            return
    cycle = hierholzer(1, edges, m)
    if len(cycle) == m+1:
        print(1)
        print(" ".join(map(str, cycle[:-1])))
    else:
        print(0)

if __name__ == "__main__":
    main()
