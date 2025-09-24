# python3
import sys
import threading


def compute_height(n, parents):
    children = [[] for _ in range(n)]
    root = 0
    for v, p in enumerate(parents):
        if p == -1:
            root = v
        else:
            children[p].append(v)

    max_h = 0
    stack = [(root, 1)]
    while stack:
        v, h = stack.pop()
        if h > max_h:
            max_h = h
        for c in children[v]:
            stack.append((c, h + 1))
    return max_h


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


sys.setrecursionlimit(10 ** 7)
threading.stack_size(2 ** 27)
threading.Thread(target=main).start()
