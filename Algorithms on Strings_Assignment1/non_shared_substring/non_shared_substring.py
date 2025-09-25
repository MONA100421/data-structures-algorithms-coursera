# Uses python3
import sys

# Reuse suffix array -> suffix tree builder from the suffix_tree solution
class Node:
    __slots__ = ("parent", "depth", "start", "end", "children", "has_p", "has_q")
    def __init__(self, parent, depth, start, end):
        self.parent = parent
        self.depth = depth
        self.start = start
        self.end = end
        self.children = {}
        self.has_p = False
        self.has_q = False

def suffix_array(s):
    n = len(s)
    order = list(range(n))
    order.sort(key=lambda i: s[i])
    classes = [0]*n
    for i in range(1, n):
        classes[order[i]] = classes[order[i-1]] + (s[order[i]] != s[order[i-1]])
    k = 1
    while (1 << k) < 2*n:
        order.sort(key=lambda i: (classes[i], classes[(i + (1 << (k-1))) % n]))
        new_classes = [0]*n
        for i in range(1, n):
            cur = (classes[order[i]], classes[(order[i] + (1 << (k-1))) % n])
            prev = (classes[order[i-1]], classes[(order[i-1] + (1 << (k-1))) % n])
            new_classes[order[i]] = new_classes[order[i-1]] + (cur != prev)
        classes = new_classes
        k += 1
        if classes[order[-1]] == n - 1:
            break
    return order

def lcp_array(s, sa):
    n = len(s)
    rank = [0]*n
    for i, pos in enumerate(sa):
        rank[pos] = i
    lcp = [0]*n
    k = 0
    for i in range(n):
        r = rank[i]
        if r == n-1:
            k = 0
            continue
        j = sa[r+1]
        while i+k < n and j+k < n and s[i+k] == s[j+k]:
            k += 1
        lcp[r+1] = k
        if k:
            k -= 1
    return lcp

class _N(Node): pass  # just to hint different usage in helpers

def create_leaf(nodes, s, parent, suffix):
    start = suffix + nodes[parent].depth
    leaf = Node(parent, len(s) - suffix, start, len(s))
    nodes.append(leaf)
    nodes[parent].children[s[start]] = len(nodes) - 1
    return len(nodes) - 1

def break_edge(nodes, s, parent, start, offset):
    child_id = nodes[parent].children[s[start]]
    child = nodes[child_id]
    mid = Node(parent, nodes[parent].depth + offset, start, start + offset)
    nodes.append(mid)
    mid_id = len(nodes) - 1
    nodes[parent].children[s[start]] = mid_id
    child.parent = mid_id
    child.start += offset
    nodes[mid_id].children[s[child.start]] = child_id
    return mid_id

def build_tree_from_sa(s, sa, lcp):
    nodes = [Node(-1, 0, -1, -1)]
    stack = [0]
    for i in range(len(sa)):
        lcp_prev = lcp[i] if i > 0 else 0
        while nodes[stack[-1]].depth > lcp_prev:
            stack.pop()
        parent = stack[-1]
        if nodes[parent].depth < lcp_prev:
            start = sa[i-1] + nodes[parent].depth
            offset = lcp_prev - nodes[parent].depth
            parent = break_edge(nodes, s, parent, start, offset)
            stack.append(parent)
        leaf = create_leaf(nodes, s, parent, sa[i])
        stack.append(leaf)
    return nodes

def mark_sets(nodes, s, p_len):
    """
    Post-order traversal to mark for each node whether it has
    a suffix from p (pos < p_len) or from q (pos > p_len).
    """
    n = len(nodes)
    sys.setrecursionlimit(max(1000000, n*2 + 10))

    def dfs(u):
        node = nodes[u]
        if not node.children:
            pos = len(s) - node.depth
            if pos < p_len:
                node.has_p = True
            elif pos > p_len:  # skip the separator '#'
                node.has_q = True
            return node.has_p, node.has_q
        hp = hq = False
        for v in node.children.values():
            cp, cq = dfs(v)
            hp = hp or cp
            hq = hq or cq
        node.has_p, node.has_q = hp, hq
        return hp, hq

    dfs(0)

def shortest_non_shared(p, q):
    s = p + "#" + q + "$"
    sa = suffix_array(s)
    lcp = lcp_array(s, sa)
    nodes = build_tree_from_sa(s, sa, lcp)
    mark_sets(nodes, s, len(p))

    best = None

    def dfs(u, path):
        nonlocal best
        node = nodes[u]
        for ch, v in node.children.items():
            child = nodes[v]
            # 若 v 子樹只含 p 的後綴，第一個跨入該子樹的字元即為最短非共享子字串的延伸
            if child.has_p and not child.has_q:
                cand = path + s[child.start]  # first char on the edge
                if best is None or len(cand) < len(best):
                    best = cand
            # 繼續往下
            edge_label = s[child.start:child.end]
            dfs(v, path + edge_label)

    dfs(0, "")
    return best if best is not None else p[0]

def solve():
    data = sys.stdin.read().split()
    p = data[0].strip()
    q = data[1].strip()
    ans = shortest_non_shared(p, q)
    print(ans)

if __name__ == "__main__":
    solve()
