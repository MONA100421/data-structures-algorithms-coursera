# python3
import itertools

EPS = 1e-9

def gaussian(a, b):
    n, m = len(a), len(a[0])
    where = [-1]*m
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
                    a[i][j] -= factor*a[col][j]
                b[i] -= factor*b[col]
        where[col] = col
    return b

def solve_diet_problem(n, m, A, b, c):
    # constraints + non-negativity
    constraints = []
    for i in range(n):
        constraints.append((A[i], b[i]))
    for j in range(m):
        vec = [0]*m
        vec[j] = -1
        constraints.append((vec, 0))
    # add big bound constraint
    bigM = 1e9
    constraints.append(([1]*m, bigM))

    best = None
    bestx = None
    # try all subsets of size m
    for rows in itertools.combinations(range(len(constraints)), m):
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
        if all(sum(ai[j]*sol[j] for j in range(m)) <= bi+1e-3 for ai,bi in constraints):
            val = sum(c[j]*sol[j] for j in range(m))
            if best is None or val > best:
                best = val
                bestx = sol
    if bestx is None:
        return -1, []
    if sum(bestx) > 1e8:
        return 1, []
    return 0, bestx

if __name__ == "__main__":
    n, m = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(n)]
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    status, sol = solve_diet_problem(n, m, A, b, c)
    if status == -1:
        print("No solution")
    elif status == 1:
        print("Infinity")
    else:
        print("Bounded solution")
        print(" ".join("{0:.18f}".format(x) for x in sol))
