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

def is_bst(n, keys, left, right):
    if n == 0:
        return True
    # stack of (node, min_allowed, max_allowed) where range is [min_allowed, max_allowed)
    stack = [(0, -float("inf"), float("inf"))]
    while stack:
        v, lo, hi = stack.pop()
        k = keys[v]
        if not (lo <= k < hi):
            return False
        if right[v] != -1:
            # right subtree: [k, hi)
            stack.append((right[v], k, hi))
        if left[v] != -1:
            # left subtree: [lo, k)
            stack.append((left[v], lo, k))
    return True

def main():
    n, keys, left, right = read_tree()
    print("CORRECT" if is_bst(n, keys, left, right) else "INCORRECT")

if __name__ == "__main__":
    main()
