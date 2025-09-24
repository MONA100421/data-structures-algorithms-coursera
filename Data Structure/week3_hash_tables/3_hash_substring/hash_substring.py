# python3
import sys
P = 1_000_000_007
X = 263

def pre_hash(s):
    n = len(s)
    H = [0]*(n+1)
    powx = [1]*(n+1)
    for i in range(1, n+1):
        H[i] = (H[i-1]*X + ord(s[i-1])) % P
        powx[i] = (powx[i-1]*X) % P
    return H, powx

def get_hash(H, powx, l, r):  # [l, r)
    return (H[r] - H[l]*powx[r-l]) % P

def main():
    data = [line.strip() for line in sys.stdin if line.strip()!='']
    if len(data) == 1:
        pat, text = data[0].split()
    else:
        pat, text = data[0], data[1]
    m, n = len(pat), len(text)
    if m > n:
        print()
        return
    Hp, powp = pre_hash(pat)
    Ht, powt = pre_hash(text)
    hp = get_hash(Hp, powp, 0, m)
    ans = []
    for i in range(n-m+1):
        if get_hash(Ht, powt, i, i+m) == hp:
            if text[i:i+m] == pat:
                ans.append(i)
    print(' '.join(map(str, ans)))

if __name__ == "__main__":
    main()
