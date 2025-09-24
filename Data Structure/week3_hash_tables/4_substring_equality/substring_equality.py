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

def eq(H1, pow1, H2, pow2, a, b, l):
    return (get_hash(H1, pow1, P1, a, a+l) == get_hash(H1, pow1, P1, b, b+l) and
            get_hash(H2, pow2, P2, a, a+l) == get_hash(H2, pow2, P2, b, b+l))

def main():
    s = sys.stdin.readline().strip()
    q = int(sys.stdin.readline())
    H1, pow1 = pre_hash(s, P1)
    H2, pow2 = pre_hash(s, P2)
    out = []
    for _ in range(q):
        a,b,l = map(int, sys.stdin.readline().split())
        out.append('Yes' if eq(H1, pow1, H2, pow2, a, b, l) else 'No')
    print('\n'.join(out))

if __name__ == "__main__":
    main()
