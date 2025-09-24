#!/usr/bin/env python3
import sys

def read_tree():
    data = sys.stdin.read().strip().split()
    if not data:
        return 0, [], [], []
    it = iter(data)
    n = int(next(it))
    keys = [0]*n
    left = [0]*n
    right = [0]*n
    for i in range(n):
        keys[i] = int(next(it)); left[i] = int(next(it)); right[i] = int(next(it))
    return n, keys, left, right

def is_bst_hard(n, keys, left, right):
    if n == 0:
        return True
    stack = [(0, -float("inf"), float("inf"))]  # range [lo, hi)
    while stack:
        v, lo, hi = stack.pop()
        k = keys[v]
        if not (lo <= k < hi):
            return False
        if right[v] != -1:
            stack.append((right[v], k, hi))   # allow == k on right
        if left[v] != -1:
            stack.append((left[v], lo, k))   # strictly less
    return True

def main():
    n, keys, left, right = read_tree()
    print("CORRECT" if is_bst_hard(n, keys, left, right) else "INCORRECT")

if __name__ == "__main__":
    main()
