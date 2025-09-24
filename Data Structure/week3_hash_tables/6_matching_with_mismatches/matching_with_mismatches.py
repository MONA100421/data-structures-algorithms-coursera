# python3
import sys

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

def equal(Ht1, Pt1, Ht2, Pt2, i, j, L):
    return (get_hash(Ht1, Pt1, P1, i, i+L) == get_hash(Ht1, Pt1, P1, j, j+L) and
            get_hash(Ht2, Pt2, P2, i, i+L) == get_hash(Ht2, Pt2, P2, j, j+L))

def lcp_with_hash(T1, P1t, T2, P2t, A1, Ap1, A2, Ap2, i, j, maxL):
    lo, hi = 0, maxL
    while lo <= hi:
        mid = (lo + hi) // 2
        if equal(T1, P1t, T2, P2t, i, j, mid):
            lo = mid + 1
        else:
            hi = mid - 1
    return hi

def solve(k, text, pattern):
    n, m = len(text), len(pattern)
    if m == 0:
        return list(range(n+1))
    if m > n:
        return []

    Ht1, Pt1 = pre_hash(text, P1)
    Ht2, Pt2 = pre_hash(text, P2)
    Hp1, Pp1 = pre_hash(pattern, P1)
    Hp2, Pp2 = pre_hash(pattern, P2)

    ans = []
    for start in range(n - m + 1):
        mism = 0
        idx = 0
        while idx < m and mism <= k:
            l = lcp_with_hash(Ht1, Pt1, Ht2, Pt2,
                              Hp1, Pp1, Hp2, Pp2,
                              start + idx, idx, m - idx)
            idx += l
            if idx >= m:
                break
            mism += 1
            idx += 1
        if mism <= k and idx >= m:
            ans.append(start)
    return ans

def main():
    lines = [l.strip() for l in sys.stdin if l.strip()]
    if not lines:
        return
    k, t, p = lines[0].split()
    k = int(k)
    res = solve(k, t, p)
    print(len(res), *res)

if __name__ == "__main__":
    main()
