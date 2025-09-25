# Uses python3
import sys

def build_trie_with_terminals(patterns):
    trie = [dict()]
    terminal = [False]
    for p in patterns:
        v = 0
        for ch in p:
            if ch not in trie[v]:
                trie[v][ch] = len(trie)
                trie.append(dict())
                terminal.append(False)
            v = trie[v][ch]
        terminal[v] = True
    return trie, terminal

def match_from(text, start, trie, terminal):
    v = 0
    i = start
    while True:
        if terminal[v]:
            return True
        if i >= len(text):
            return False
        ch = text[i]
        if ch in trie[v]:
            v = trie[v][ch]
            i += 1
        else:
            return False

def solve():
    data = sys.stdin.read().strip().split()
    text = data[0]
    n = int(data[1])
    patterns = data[2:]
    trie, terminal = build_trie_with_terminals(patterns)
    out = []
    for i in range(len(text)):
        if match_from(text, i, trie, terminal):
            out.append(i)
    print(" ".join(map(str, out)))

if __name__ == "__main__":
    solve()
