#!/usr/bin/env python3
# Coursera: Set with range sums using Splay Tree
import sys

MOD = 10**9 + 1

class Node:
    __slots__ = ("key", "sum", "left", "right", "parent")
    def __init__(self, key, left=None, right=None, parent=None):
        self.key = key
        self.sum = key
        self.left = left
        self.right = right
        self.parent = parent

def get_sum(v):
    return 0 if v is None else v.sum

def update(v):
    if v is None:
        return
    v.sum = v.key + get_sum(v.left) + get_sum(v.right)
    if v.left:
        v.left.parent = v
    if v.right:
        v.right.parent = v

def small_rotation(v):
    parent = v.parent
    if parent is None:
        return
    grandparent = parent.parent
    if parent.left == v:
        m = v.right
        v.right = parent
        parent.left = m
    else:
        m = v.left
        v.left = parent
        parent.right = m
    update(parent)
    update(v)
    v.parent = grandparent
    if grandparent:
        if grandparent.left == parent:
            grandparent.left = v
        else:
            grandparent.right = v

def big_rotation(v):
    if v.parent.left == v and v.parent.parent.left == v.parent:
        # zig-zig
        small_rotation(v.parent)
        small_rotation(v)
    elif v.parent.right == v and v.parent.parent.right == v.parent:
        # zig-zig
        small_rotation(v.parent)
        small_rotation(v)
    else:
        # zig-zag
        small_rotation(v)
        small_rotation(v)

def splay(v):
    if v is None:
        return None
    while v.parent:
        if v.parent.parent is None:
            small_rotation(v)
            break
        big_rotation(v)
    return v

def find(root, key):
    v = root
    last = root
    next_ = None
    while v:
        if v.key >= key and (next_ is None or v.key < next_.key):
            next_ = v
        last = v
        if v.key == key:
            break
        if key < v.key:
            v = v.left
        else:
            v = v.right
    root = splay(last)
    return (root, next_)

def split(root, key):
    if root is None:
        return (None, None)
    root, result = find(root, key)
    if result is None:
        return (root, None)
    root = splay(result)
    left = root.left
    if left:
        left.parent = None
    root.left = None
    update(left)
    update(root)
    return (left, root)

def merge(left, right):
    if left is None:
        return right
    if right is None:
        return left
    # find max in left
    v = left
    while v.right:
        v = v.right
    left = splay(v)
    left.right = right
    if right:
        right.parent = left
    update(left)
    return left

class SplaySet:
    def __init__(self):
        self.root = None

    def search(self, key):
        self.root, node = find(self.root, key)
        self.root = splay(node if node else self.root)
        return node is not None and node.key == key

    def insert(self, key):
        (left, right) = split(self.root, key)
        if right and right.key == key:
            self.root = merge(left, right)
            return
        new = Node(key)
        self.root = merge(merge(left, new), right)

    def erase(self, key):
        if self.root is None:
            return
        self.root, node = find(self.root, key)
        if node is None or node.key != key:
            return
        self.root = splay(node)
        left = self.root.left
        right = self.root.right
        if left:
            left.parent = None
        if right:
            right.parent = None
        self.root = merge(left, right)

    def range_sum(self, l, r):
        if self.root is None:
            return 0
        left, mid = split(self.root, l)
        mid, right = split(mid, r + 1)
        ans = get_sum(mid)
        self.root = merge(left, merge(mid, right))
        return ans

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    st = SplaySet()
    last_sum_result = 0
    out = []
    for _ in range(q):
        typ = next(it)
        if typ == "+":
            x = (int(next(it)) + last_sum_result) % MOD
            st.insert(x)
        elif typ == "-":
            x = (int(next(it)) + last_sum_result) % MOD
            st.erase(x)
        elif typ == "?":
            x = (int(next(it)) + last_sum_result) % MOD
            out.append("Found" if st.search(x) else "Not found")
        else:  # 's'
            l = (int(next(it)) + last_sum_result) % MOD
            r = (int(next(it)) + last_sum_result) % MOD
            if l > r:
                l, r = r, l
            s = st.range_sum(l, r)
            out.append(str(s))
            last_sum_result = s % MOD
    print("\n".join(out))

if __name__ == "__main__":
    main()
