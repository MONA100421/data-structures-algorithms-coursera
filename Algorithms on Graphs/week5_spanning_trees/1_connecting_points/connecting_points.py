# Uses python3
import sys
import math

def minimum_distance(x, y):
    n = len(x)
    used = [False] * n
    key = [float('inf')] * n
    key[0] = 0.0
    result = 0.0

    for _ in range(n):
        u = -1
        u_key = float('inf')
        for v in range(n):
            if not used[v] and key[v] < u_key:
                u, u_key = v, key[v]

        used[u] = True
        result += u_key

        for v in range(n):
            if not used[v]:
                d = math.hypot(x[u] - x[v], y[u] - y[v])
                if d < key[v]:
                    key[v] = d

    return result


if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
