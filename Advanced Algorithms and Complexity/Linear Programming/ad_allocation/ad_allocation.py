# python3
from diet import solve_diet_problem

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
        print(" ".join("{0:.18f}".format(x) for x in sol)))
