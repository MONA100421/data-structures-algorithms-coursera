# python3
from itertools import combinations
import sys

EPS = 1e-9
INF = 1e9

def gaussian(a, b):
    n, m = len(a), len(a[0])
    where = [-1] * m
    for col in range(m):
        sel = -1
        for row in range(col, n):
            if abs(a[row][col]) > EPS:
                sel = row
                break
        if sel == -1:
            continue
        a[col], a[sel] = a[sel], a[col]
        b[col], b[sel] = b[sel], b[col]
        div = a[col][col]
        for j in range(col, m):
            a[col][j] /= div
        b[col] /= div
        for i in range(n):
            if i != col:
                factor = a[i][col]
                for j in range(col, m):
                    a[i][j] -= factor * a[col][j]
                b[i] -= factor * b[col]
        where[col] = col
    return b

def solve_diet_problem(n, m, A, b, c):
    constraints = []
    for i in range(n):
        constraints.append((A[i], b[i]))
    for j in range(m):  # xj >= 0
        vec = [0]*m
        vec[j] = -1
        constraints.append((vec, 0))
    # sum xi <= big bound
    constraints.append(([1]*m, INF))

    best_val = None
    best_sol = None

    for rows in combinations(range(len(constraints)), m):
        a = []
        bb = []
        for r in rows:
            a.append(list(constraints[r][0]))
            bb.append(constraints[r][1])
        try:
            sol = gaussian([row[:] for row in a], bb[:])
        except:
            continue
        if any(x < -EPS for x in sol):
            continue
        ok = True
        for ai, bi in constraints:
            if sum(ai[j]*sol[j] for j in range(m)) > bi + 1e-6:
                ok = False
                break
        if not ok:
            continue
        val = sum(c[j]*sol[j] for j in range(m))
        if best_val is None or val > best_val:
            best_val = val
            best_sol = sol

    if best_sol is None:
        return -1, []
    if sum(best_sol) > INF/2:
        return 1, []
    return 0, best_sol

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    A = []
    for _ in range(n):
        A.append(list(map(int, sys.stdin.readline().split())))
    b = list(map(int, sys.stdin.readline().split()))
    c = list(map(int, sys.stdin.readline().split()))

    status, sol = solve_diet_problem(n, m, A, b, c)
    if status == -1:
        print("No solution")
    elif status == 1:
        print("Infinity")
    else:
        print("Bounded solution")
        print(" ".join("{0:.18f}".format(x) for x in sol))
