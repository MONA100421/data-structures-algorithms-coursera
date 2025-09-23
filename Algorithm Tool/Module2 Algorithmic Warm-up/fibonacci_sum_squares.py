import sys
n = int(sys.stdin.read())

def fib_pair_mod(n: int, mod: int):
    def fd(k: int):
        if k == 0:
            return (0, 1)
        a, b = fd(k >> 1)
        c = (a * ((2*b - a) % mod)) % mod
        d = (a*a + b*b) % mod
        return (d, (c + d) % mod) if (k & 1) else (c, d)
    return fd(n)

fn, fn1 = fib_pair_mod(n, 10)
print((fn * fn1) % 10)
