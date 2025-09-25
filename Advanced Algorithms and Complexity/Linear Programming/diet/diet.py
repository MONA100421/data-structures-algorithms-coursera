# python3
from sys import stdin
import itertools

EPS = 1e-9

def gauss(A, b):
    n, m = len(A), len(A[0])
    for col in range(m):
        sel = col
        for row in range(col, n):
            if abs(A[row][col]) > abs(A[sel][col]):
                sel = row
        if abs(A[sel][col]) < EPS:
            continue
        A[col], A[sel] = A[sel], A[col]
        b[col], b[sel] = b[sel], b[col]
        div = A[col][col]
        for j in range(col, m):
            A[col][j] /= div
        b[col] /= div
        for row in range(n):
            if row != col:
                factor = A[row][col]
                for j in range(col, m):
                    A[row][j] -= factor * A[col][j]
                b[row] -= factor * b[col]
    return b

def solve_diet_problem(n, m, A, b, c):
    # Add non-negativity constraints
    for i in range(m):
        row = [0]*m
        row[i] = -1
        A.append(row)
        b.append(0)
    n = len(A)
    best_val = None
    best_sol = None
    for subset in itertools.combinations(range(n), m):
        subA = [A[i][:] for i in subset]
        subb = [b[i] for i in subset]
        try:
            sol = gauss([row[:] for row in subA], subb[:])
        except:
            continue
        if any(x < -EPS for x in sol):
            continue
        if any(sum(A[i][j] * sol[j] for j in range(m)) - b[i] > EPS for i in range(n)):
            continue
        val = sum(c[j] * sol[j] for j in range(m))
        if best_val is None or val > best_val + EPS:
            best_val = val
            best_sol = sol
    if best_sol is None:
        return [-1, []]
    if best_val > 1e18:
        return [1, []]
    return [0, best_sol]

if __name__ == '__main__':
    n, m = list(map(int, stdin.readline().split()))
    A = []
    for _ in range(n):
        A.append(list(map(int, stdin.readline().split())))
    b = list(map(int, stdin.readline().split()))
    c = list(map(int, stdin.readline().split()))
    anst, ansx = solve_diet_problem(n, m, A, b, c)
    if anst == -1:
        print("No solution")
    if anst == 0:
        print("Bounded solution")
        print(' '.join(list(map(lambda x: '%.18f' % x, ansx))))
    if anst == 1:
        print("Infinity")
