import sys
n, m = map(int, sys.stdin.read().split())

def fib_mod(n: int, mod: int) -> int:
    def fd(k: int):
        if k == 0:
            return (0, 1)
        a, b = fd(k >> 1)                    # a=F(t), b=F(t+1)
        c = (a * ((2*b - a) % mod)) % mod    # F(2t)
        d = (a*a + b*b) % mod                # F(2t+1)
        return (d, (c + d) % mod) if (k & 1) else (c, d)
    return fd(n)[0]

print(fib_mod(n, m))
