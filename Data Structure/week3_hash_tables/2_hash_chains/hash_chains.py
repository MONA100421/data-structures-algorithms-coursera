# python3
import sys

P = 1_000_000_007
X = 263

def poly_hash(s):
    h = 0
    for c in reversed(s):
        h = (h * X + ord(c)) % P
    return h

def main():
    m = int(sys.stdin.readline())
    chains = [[] for _ in range(m)]
    q = int(sys.stdin.readline())
    out = []
    for _ in range(q):
        parts = sys.stdin.readline().split()
        t = parts[0]
        if t == 'check':
            idx = int(parts[1])
            out.append(' '.join(chains[idx]))
        else:
            s = parts[1]
            h = poly_hash(s) % m
            chain = chains[h]
            if t == 'find':
                out.append('yes' if s in chain else 'no')
            elif t == 'add':
                if s not in chain:
                    chain.insert(0, s)
            else:  # del
                try:
                    chain.remove(s)
                except ValueError:
                    pass
    print('\n'.join(out))

if __name__ == "__main__":
    main()
