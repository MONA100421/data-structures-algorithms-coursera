# python3
import sys
from itertools import combinations

def var(i, j, n):
    # 節點 i 在位置 j 的變數 index
    return i * n + j + 1

def printEquisatisfiableSatFormula():
    n, m = map(int, sys.stdin.readline().split())
    edges = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
    adj = [[False]*n for _ in range(n)]
    for u, v in edges:
        adj[u-1][v-1] = True
        adj[v-1][u-1] = True

    clauses = []

    # 每個位置必須有一個頂點
    for j in range(n):
        clauses.append([var(i,j,n) for i in range(n)])
        for i1,i2 in combinations(range(n),2):
            clauses.append([-var(i1,j,n), -var(i2,j,n)])

    # 每個頂點必須出現一次
    for i in range(n):
        clauses.append([var(i,j,n) for j in range(n)])
        for j1,j2 in combinations(range(n),2):
            clauses.append([-var(i,j1,n), -var(i,j2,n)])

    # 相鄰位置必須是有邊的
    for j in range(n-1):
        for i1 in range(n):
            for i2 in range(n):
                if not adj[i1][i2]:
                    clauses.append([-var(i1,j,n), -var(i2,j+1,n)])

    print(len(clauses), n*n)
    for c in clauses:
        print(" ".join(map(str,c)), "0")

if __name__ == "__main__":
    printEquisatisfiableSatFormula()
