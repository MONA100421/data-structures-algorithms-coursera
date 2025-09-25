# python3
# Use suffix array to find all pattern occurrences.
# Input:
#   text (ends with '$')
#   n
#   n patterns
# Output:
#   all starting positions (0-based, space-separated) of any pattern in text, sorted, unique

import sys

def build_suffix_array(s: str):
    """ O(n log n) suffix-array by doubling. """
    n = len(s)
    k = 1
    sa = list(range(n))
    rank = [ord(c) for c in s]
    tmp = [0] * n
    while True:
        sa.sort(key=lambda i: (rank[i], rank[i + k] if i + k < n else -1))
        tmp[sa[0]] = 0
        for i in range(1, n):
            prev, cur = sa[i - 1], sa[i]
            tmp[cur] = tmp[prev] + (rank[cur] != rank[prev] or
                                    (rank[cur + k] if cur + k < n else -1) !=
                                    (rank[prev + k] if prev + k < n else -1))
        rank, tmp = tmp, rank
        if rank[sa[-1]] == n - 1:
            break
        k <<= 1
    return sa

def cmp_prefix(s: str, pos: int, pat: str):
    """Compare pat with suffix s[pos:]. return -1 if pat < suffix,
       1 if pat > suffix prefix, 0 if pat is a prefix of suffix."""
    i = 0
    while i < len(pat) and pos + i < len(s):
        if pat[i] != s[pos + i]:
            return -1 if pat[i] < s[pos + i] else 1
        i += 1
    if i == len(pat):
        return 0
    return 1  # pat longer than suffix -> pat > suffix

def find_occurrences(text: str, sa, pat: str):
    n = len(text)
    # left boundary
    lo, hi = 0, n
    while lo < hi:
        mid = (lo + hi) // 2
        c = cmp_prefix(text, sa[mid], pat)
        if c == 1:  # pat > suffix
            lo = mid + 1
        else:
            hi = mid
    l = lo
    # right boundary
    lo, hi = 0, n
    while lo < hi:
        mid = (lo + hi) // 2
        c = cmp_prefix(text, sa[mid], pat)
        if c == -1:  # pat < suffix
            hi = mid
        else:
            lo = mid + 1
    r = lo
    # matches are sa[l:r] where pat is prefix of suffix
    return [sa[i] for i in range(l, r) if text.startswith(pat, sa[i])]

def main():
    data = sys.stdin.read().split()
    text = data[0]
    m = int(data[1])
    patterns = data[2:2 + m]
    sa = build_suffix_array(text)
    ans = set()
    for p in patterns:
        for pos in find_occurrences(text, sa, p):
            ans.add(pos)
    print(*sorted(ans))

if __name__ == "__main__":
    main()
