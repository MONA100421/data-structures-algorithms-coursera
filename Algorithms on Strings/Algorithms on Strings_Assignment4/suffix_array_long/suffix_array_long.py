# python3
# Longest Common Substring (of two strings) using suffix array + Kasai LCP.
# Input:
#   s
#   t
# Output:
#   one longest common substring (if multiple, any one is fine; grader accepts any)

import sys

def build_suffix_array(s: str):
    n = len(s)
    k = 1
    sa = list(range(n))
    rank = [ord(c) for c in s]
    tmp = [0] * n
    while True:
        sa.sort(key=lambda i: (rank[i], rank[i + k] if i + k < n else -1))
        tmp[sa[0]] = 0
        for i in range(1, n):
            a, b = sa[i-1], sa[i]
            tmp[b] = tmp[a] + (rank[a] != rank[b] or
                              (rank[a + k] if a + k < n else -1) !=
                              (rank[b + k] if b + k < n else -1))
        rank, tmp = tmp, rank
        if rank[sa[-1]] == n - 1:
            break
        k <<= 1
    return sa

def kasai_lcp(s: str, sa):
    n = len(s)
    rank = [0] * n
    for i, p in enumerate(sa):
        rank[p] = i
    lcp = [0] * (n - 1)
    k = 0
    for i in range(n):
        r = rank[i]
        if r == n - 1:
            k = 0
            continue
        j = sa[r + 1]
        while i + k < n and j + k < n and s[i + k] == s[j + k]:
            k += 1
        lcp[r] = k
        if k:
            k -= 1
    return lcp

def longest_common_substring(a: str, b: str):
    sep1 = '\x01'
    sep2 = '\x02'
    s = a + sep1 + b + sep2
    n1 = len(a)
    sa = build_suffix_array(s)
    lcp = kasai_lcp(s, sa)
    best_len, best_pos = 0, 0
    for i in range(len(lcp)):
        x, y = sa[i], sa[i+1]
        in_a = x < n1
        in_b = y < n1
        if in_a == in_b:  # both from same string
            continue
        if lcp[i] > best_len:
            best_len = lcp[i]
            best_pos = sa[i]
    return s[best_pos:best_pos + best_len] if best_len > 0 else ""

def main():
    data = sys.stdin.read().splitlines()
    a = data[0].rstrip('\n')
    b = data[1].rstrip('\n') if len(data) > 1 else ""
    print(longest_common_substring(a, b))

if __name__ == "__main__":
    main()
