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

def inorder(n, keys, left, right):
    if n == 0:
        return []
    res = []
    stack = []
    cur = 0
    while stack or cur != -1:
        while cur != -1:
            stack.append(cur)
            cur = left[cur]
        cur = stack.pop()
        res.append(keys[cur])
        cur = right[cur]
    return res

def preorder(n, keys, left, right):
    if n == 0:
        return []
    res = []
    stack = [0]
    while stack:
        v = stack.pop()
        res.append(keys[v])
        r = right[v]
        l = left[v]
        if r != -1:
            stack.append(r)
        if l != -1:
            stack.append(l)
    return res

def postorder(n, keys, left, right):
    if n == 0:
        return []
    res = []
    stack = []
    cur = 0
    last = -1
    while stack or cur != -1:
        if cur != -1:
            stack.append(cur)
            cur = left[cur]
        else:
            peek = stack[-1]
            r = right[peek]
            if r != -1 and last != r:
                cur = r
            else:
                res.append(keys[peek])
                last = stack.pop()
    return res

def main():
    n, keys, left, right = read_tree()
    sys.setrecursionlimit(1 << 25)
    print(*inorder(n, keys, left, right))
    print(*preorder(n, keys, left, right))
    print(*postorder(n, keys, left, right))

if __name__ == "__main__":
    main()
