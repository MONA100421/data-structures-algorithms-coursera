# python3
# Knuth–Morris–Pratt pattern matching.
# Input:
#   pattern
#   text
# Output:
#   all starting positions (0-based, space-separated) of pattern in text

import sys

def prefix_function(s: str):
    pi = [0] * len(s)
    j = 0
    for i in range(1, len(s)):
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi

def kmp(pattern: str, text: str):
    if not pattern:
        return list(range(len(text) + 1))
    sep = '\x01'  # a char not in input alphabet
    s = pattern + sep + text
    pi = prefix_function(s)
    m = len(pattern)
    res = []
    for i in range(m + 1, len(s)):
        if pi[i] == m:
            res.append(i - 2 * m)
    return res

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    pattern = data[0].rstrip('\n')
    text = data[1].rstrip('\n') if len(data) > 1 else ""
    ans = kmp(pattern, text)
    print(*ans)

if __name__ == "__main__":
    main()
