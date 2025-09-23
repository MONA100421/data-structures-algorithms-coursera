def evaluate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        raise ValueError("Unknown operator: %r" % op)


def maximum_value(dataset: str) -> int:
    # Parse digits and operators
    digits = list(map(int, dataset[::2]))
    ops = list(dataset[1::2])
    n = len(digits)
    # min/max tables for subexpressions i..j
    mn = [[0]*n for _ in range(n)]
    mx = [[0]*n for _ in range(n)]
    for i in range(n):
        mn[i][i] = mx[i][i] = digits[i]

    for s in range(1, n):               # s = subexpr length - 1
        for i in range(0, n - s):
            j = i + s
            cur_min = float('inf')
            cur_max = -float('inf')
            for k in range(i, j):
                op = ops[k]
                a = evaluate(mx[i][k], mx[k+1][j], op)
                b = evaluate(mx[i][k], mn[k+1][j], op)
                c = evaluate(mn[i][k], mx[k+1][j], op)
                d = evaluate(mn[i][k], mn[k+1][j], op)
                cur_min = min(cur_min, a, b, c, d)
                cur_max = max(cur_max, a, b, c, d)
            mn[i][j] = cur_min
            mx[i][j] = cur_max
    return mx[0][n-1]


if __name__ == "__main__":
    print(maximum_value(input().strip()))
