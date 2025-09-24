# python3
import sys
from collections import namedtuple

Ans = namedtuple('Ans', 'i j length')

P1, P2 = 1_000_000_007, 1_000_000_009
X = 911382323

def pre_hash(s, P):
    n = len(s)
    H = [0]*(n+1)
    powx = [1]*(n+1)
    for i in range(1, n+1):
        H[i] = (H[i-1]*X + ord(s[i-1])) % P
        powx[i] = (powx[i-1]*X) % P
    return H, powx

def get_hash(H, powx, P, l, r):  # [l,r)
    return (H[r] - H[l]*powx[r-l]) % P

def collect_hashes(s, H1, pw1, H2, pw2, L):
    seen = {}
    if L == 0:
        return seen
    n = len(s)
    for i in range(n-L+1):
        h1 = get_hash(H1, pw1, P1, i, i+L)
        h2 = get_hash(H2, pw2, P2, i, i+L)
        seen.setdefault((h1,h2), i)
    return seen

def longest_common_substring(s, t):
    H1s, pw1s = pre_hash(s, P1)
    H2s, pw2s = pre_hash(s, P2)
    H1t, pw1t = pre_hash(t, P1)
    H2t, pw2t = pre_hash(t, P2)

    lo, hi = 0, min(len(s), len(t))
    ans = Ans(0,0,0)
    while lo <= hi:
        mid = (lo+hi)//2
        Smap = collect_hashes(s, H1s, pw1s, H2s, pw2s, mid)
        found = None
        if mid == 0:
            found = (0,0)
        else:
            for j in range(len(t)-mid+1):
                h1 = get_hash(H1t, pw1t, P1, j, j+mid)
                h2 = get_hash(H2t, pw2t, P2, j, j+mid)
                key = (h1,h2)
                if key in Smap:
                    found = (Smap[key], j)
                    break
        if found is not None:
            ans = Ans(found[0], found[1], mid)
            lo = mid + 1
        else:
            hi = mid - 1
    return ans

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        s, t = line.split()
        a = longest_common_substring(s, t)
        print(a.i, a.j, a.length)

if __name__ == "__main__":
    main()
