# Uses python3
import sys

def build_trie(patterns):
    """
    Construct a trie from patterns.
    Returns list of nodes, where each node is a dict: {char: child_index}.
    Node 0 is the root.
    """
    trie = [dict()]
    for p in patterns:
        v = 0
        for ch in p:
            if ch not in trie[v]:
                trie[v][ch] = len(trie)
                trie.append(dict())
            v = trie[v][ch]
        # Mark terminal explicitly (support a pattern being a prefix of another)
        if '$' not in trie[v]:
            trie[v]['$'] = -1  # terminal marker (no actual edge)
    return trie

def solve():
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    patterns = data[1:]
    trie = build_trie(patterns)
    out = []
    for i, edges in enumerate(trie):
        for ch, j in edges.items():
            if ch == '$':
                continue
            out.append(f"{i}->{j}:{ch}")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
