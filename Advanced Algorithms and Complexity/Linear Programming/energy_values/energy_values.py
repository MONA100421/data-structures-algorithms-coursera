# python3
EPS = 1e-9

def read_equation():
    size = int(input())
    a = []
    b = []
    for row in range(size):
        line = list(map(float, input().split()))
        a.append(line[:size])
        b.append(line[size])
    return a, b

def select_pivot(a, used_rows, used_cols):
    n = len(a)
    for r in range(n):
        if not used_rows[r]:
            for c in range(n):
                if not used_cols[c]:
                    return r, c
    return None, None

def swap_lines(a, b, used_rows, pivot):
    r, c = pivot
    if r != c:
        a[r], a[c] = a[c], a[r]
        b[r], b[c] = b[c], b[r]
        used_rows[r], used_rows[c] = used_rows[c], used_rows[r]
    return r, c

def process_pivot(a, b, pivot):
    r, c = pivot
    n = len(a)
    m = len(a[0])
    # scale pivot row
    div = a[r][c]
    for j in range(m):
        a[r][j] /= div
    b[r] /= div
    # eliminate other rows
    for i in range(n):
        if i != r:
            factor = a[i][c]
            for j in range(m):
                a[i][j] -= factor * a[r][j]
            b[i] -= factor * b[r]

def mark_pivot(pivot, used_rows, used_cols):
    r, c = pivot
    used_rows[r] = True
    used_cols[c] = True

def solve_equation(a, b):
    n = len(a)
    used_rows = [False]*n
    used_cols = [False]*n
    for step in range(n):
        pivot = select_pivot(a, used_rows, used_cols)
        swap_lines(a, b, used_rows, pivot)
        process_pivot(a, b, pivot)
        mark_pivot(pivot, used_rows, used_cols)
    return b

def print_result(ans):
    for x in ans:
        print("{0:.20f}".format(x))

if __name__ == "__main__":
    a, b = read_equation()
    ans = solve_equation(a, b)
    print_result(ans)
