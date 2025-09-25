# python3
import sys

def printEquisatisfiableSatFormula():
    # 讀入
    n, m = map(int, sys.stdin.readline().split())
    A = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    b = list(map(int, sys.stdin.readline().split()))

    # 總共有 n 個限制，每個限制 ≤ b[i]
    # 每個限制可轉換成 SAT：不能同時選超過 b[i] + 1 個變數
    clauses = []
    num_vars = m

    for i in range(n):
        row = []
        for j in range(m):
            if A[i][j] != 0:
                row.append(j + 1)
        if len(row) > b[i]:
            # 任選 b[i]+1 個變數 → 至少一個要為 False
            from itertools import combinations
            for comb in combinations(row, b[i] + 1):
                clause = [-x for x in comb]
                clauses.append(clause)

    # 輸出 CNF
    print(len(clauses), num_vars)
    for c in clauses:
        print(" ".join(map(str, c)), "0")

if __name__ == "__main__":
    printEquisatisfiableSatFormula()
