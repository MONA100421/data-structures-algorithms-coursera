#!/usr/bin/env python3
# Rope with Splay tree (implicit keys by subtree size)
import sys

sys.setrecursionlimit(1 << 25)

class Node:
    __slots__ = ("ch", "left", "right", "parent", "size")
    def __init__(self, ch):
        self.ch = ch
        self.left = None
        self.right = None
        self.parent = None
        self.size = 1

def sz(v): return 0 if v is None else v.size

def update(v):
    if v is None: return
    v.size = 1 + sz(v.left) + sz(v.right)
    if v.left: v.left.parent = v
    if v.right: v.right.parent = v

def small_rotation(v):
    p = v.parent
    if p is None: return
    g = p.parent
    if p.left == v:
        m = v.right
        v.right = p
        p.left = m
    else:
        m = v.left
        v.left = p
        p.right = m
    update(p); update(v)
    v.parent = g
    if g:
        if g.left == p: g.left = v
        else: g.right = v

def big_rotation(v):
    if v.parent.left == v and v.parent.parent.left == v.parent:
        small_rotation(v.parent)
        small_rotation(v)
    elif v.parent.right == v and v.parent.parent.right == v.parent:
        small_rotation(v.parent)
        small_rotation(v)
    else:
        small_rotation(v)
        small_rotation(v)

def splay(v):
    if v is None: return None
    while v.parent:
        if v.parent.parent is None:
            small_rotation(v)
            break
        big_rotation(v)
    return v

def find_kth(root, k):
    """0-based index; return (new_root, node_at_k)"""
    v = root
    last = root
    while v:
        last = v
        left_size = sz(v.left)
        if k == left_size:
            root = splay(v)
            return (root, root)
        elif k < left_size:
            v = v.left
        else:
            k -= left_size + 1
            v = v.right
    root = splay(last)
    return (root, None)

def split(root, k):
    """split by index k: [0..k-1], [k..end]"""
    if root is None:
        return (None, None)
    if k <= 0:
        return (None, root)
    if k >= sz(root):
        return (root, None)
    root, node = find_kth(root, k)
    if node is None:
        return (root, None)  # shouldn't happen with bounds check
    left = node.left
    if left: left.parent = None
    node.left = None
    update(left); update(node)
    return (left, node)

def merge(left, right):
    if left is None: return right
    if right is None: return left
    # max of left
    v = left
    while v.right: v = v.right
    left = splay(v)
    left.right = right
    right.parent = left
    update(left)
    return left

def build_balanced(s, lo, hi):
    if lo > hi: return None
    mid = (lo + hi) // 2
    root = Node(s[mid])
    root.left = build_balanced(s, lo, mid - 1)
    root.right = build_balanced(s, mid + 1, hi)
    if root.left: root.left.parent = root
    if root.right: root.right.parent = root
    update(root)
    return root

def inorder_collect(v, out):
    stack = []
    cur = v
    while stack or cur:
        while cur:
            stack.append(cur); cur = cur.left
        cur = stack.pop()
        out.append(cur.ch)
        cur = cur.right

def process(root, i, j, k):
    # cut [i..j]
    left, mid_right = split(root, i)
    mid, right = split(mid_right, j - i + 1)
    root = merge(left, right)  # removed block

    if k > i:
        k -= (j - i + 1)

    left, right = split(root, k)
    root = merge(merge(left, mid), right)
    return root

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    s = data[0]
    q = int(data[1])
    idx = 2
    root = build_balanced(s, 0, len(s) - 1)
    for _ in range(q):
        i = int(data[idx]); j = int(data[idx+1]); k = int(data[idx+2]); idx += 3
        root = process(root, i, j, k)
    out = []
    inorder_collect(root, out)
    print("".join(out))

if __name__ == "__main__":
    main()
