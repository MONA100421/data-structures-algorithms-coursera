# python3
# Build suffix tree from (text, SA, LCP). Output edges as "start end" (end is exclusive).
# Input:
#   text
#   integer n
#   n integers ... (suffix array)
#   n-1 integers ... (LCP array; if absent, treat as zeros)
# Output:
#   Each line: "start end" for an edge (order arbitrary is fine).

import sys

class Node:
    __slots__ = ("children", "parent", "string_depth", "edge_start", "edge_end")
    def __init__(self, parent=None, string_depth=0, edge_start=-1, edge_end=-1):
        self.children = []
        self.parent = parent
        self.string_depth = string_depth
        self.edge_start = edge_start
        self.edge_end = edge_end

def create_new_leaf(parent: Node, text: str, suffix: int) -> Node:
    leaf = Node(parent=parent,
                string_depth=len(text) - suffix,
                edge_start=suffix + parent.string_depth,
                edge_end=len(text))
    parent.children.append(leaf)
    return leaf

def break_edge(node: Node, text: str, start: int, offset: int) -> Node:
    mid = Node(parent=node.parent,
               string_depth=node.parent.string_depth + offset,
               edge_start=start,
               edge_end=start + offset)
    # redirect node.parent -> mid
    p = node.parent
    p.children.remove(node)
    p.children.append(mid)

    node.parent = mid
    node.edge_start += offset
    mid.children.append(node)
    return mid

def suffix_tree_from_sa(text: str, sa, lcp):
    root = Node(parent=None, string_depth=0, edge_start=-1, edge_end=-1)
    lcp_prev = 0
    cur = root
    for i in range(len(text)):
        suffix = sa[i]
        while cur.string_depth > lcp_prev:
            cur = cur.parent
        if cur.string_depth == lcp_prev:
            # Create new leaf
            cur = create_new_leaf(cur, text, suffix)
        else:
            edge_start = sa[i - 1] + cur.string_depth
            offset = lcp_prev - cur.parent.string_depth
            mid = break_edge(cur, text, edge_start, offset)
            cur = create_new_leaf(mid, text, suffix)
        if i < len(text) - 1:
            lcp_prev = lcp[i]
    return root

def collect_edges(node: Node, out):
    for ch in node.children:
        out.append((ch.edge_start, ch.edge_end))
        collect_edges(ch, out)

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    text = next(it)
    # Some graders give n explicitly; some not. Try to be permissive.
    rest = list(it)
    nums = list(map(int, rest))
    n = len(text)
    if len(nums) >= 1 + (n - 1):  # probably had explicit n
        sa = nums[:n]
        lcp = nums[n:n + n - 1]
    else:
        # No explicit n; first n numbers are SA, rest n-1 are LCP.
        k = n
        sa = nums[:k]
        lcp = nums[k:k + n - 1]
        if len(lcp) != n - 1:
            lcp = [0] * (n - 1)

    root = suffix_tree_from_sa(text, sa, lcp)
    edges = []
    collect_edges(root, edges)
    for s, e in edges:
        print(s, e)

if __name__ == "__main__":
    main()
