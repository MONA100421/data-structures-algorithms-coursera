# Uses python3
import sys

class Node:
    __slots__ = ("parent", "depth", "start", "end", "children")
    def __init__(self, parent, depth, start, end):
        self.parent = parent
        self.depth = depth              # string-depth (path length from root)
        self.start = start              # start index of edge label
        self.end = end                  # end index (exclusive)
        self.children = {}              # char -> node id

def suffix_array(s):
    n = len(s)
    # initial sort by single characters
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

def create_new_leaf(nodes, s, parent, suffix):
    start = suffix + nodes[parent].depth
    leaf = Node(parent, len(s) - suffix, start, len(s))
    nodes.append(leaf)
    nodes[parent].children[s[start]] = len(nodes) - 1
    return len(nodes) - 1

def break_edge(nodes, s, parent, start, offset):
    """
    Break edge (parent -> child starting at position 'start') at 'offset' characters,
    create and return the new middle node.
    """
    child_id = nodes[parent].children[s[start]]
    child = nodes[child_id]
    mid = Node(parent, nodes[parent].depth + offset, start, start + offset)
    nodes.append(mid)
    mid_id = len(nodes) - 1

    # rewire parent -> mid
    nodes[parent].children[s[start]] = mid_id
    # rewire mid -> child
    child.parent = mid_id
    child.start += offset
    nodes[mid_id].children[s[child.start]] = child_id
    return mid_id

def build_tree_from_sa(s, sa, lcp):
    nodes = [Node(-1, 0, -1, -1)]  # root
    stack = [0]                    # stack of node ids representing the path of previous suffix
    for i in range(len(sa)):
        lcp_prev = lcp[i] if i > 0 else 0
        # Pop from stack until we find node with depth <= lcp_prev
        while nodes[stack[-1]].depth > lcp_prev:
            stack.pop()
        parent = stack[-1]
        if nodes[parent].depth < lcp_prev:
            # need to split edge and create middle node
            start = sa[i-1] + nodes[parent].depth
            offset = lcp_prev - nodes[parent].depth
            parent = break_edge(nodes, s, parent, start, offset)
            stack.append(parent)
        # add leaf for current suffix
        leaf = create_new_leaf(nodes, s, parent, sa[i])
        stack.append(leaf)
    return nodes

def solve():
    text = sys.stdin.readline().strip()
    # assume text ends with '$'
    sa = suffix_array(text)
    lcp = lcp_array(text, sa)
    nodes = build_tree_from_sa(text, sa, lcp)
    # collect edge labels
    result = []
    for i in range(1, len(nodes)):
        result.append(text[nodes[i].start:nodes[i].end])
    sys.stdout.write("\n".join(result))

if __name__ == "__main__":
    solve()
