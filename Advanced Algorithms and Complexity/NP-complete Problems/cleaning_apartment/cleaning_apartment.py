# python3

def printEquisatisfiableSatFormula():
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]

    # position[i][j] 表示 頂點 i 是否在路徑的第 j 個位置
    def var(i, j):
        return (i - 1) * n + j

    clauses = []

    # 每個頂點至少要在一個位置
    for i in range(1, n + 1):
        clauses.append([var(i, j) for j in range(1, n + 1)])

    # 每個頂點最多在一個位置
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(j + 1, n + 1):
                clauses.append([-var(i, j), -var(i, k)])

    # 每個位置只能放一個頂點
    for j in range(1, n + 1):
        for i in range(1, n + 1):
            for k in range(i + 1, n + 1):
                clauses.append([-var(i, j), -var(k, j)])

    # 非鄰接頂點不可相鄰
    adj = [[False] * (n + 1) for _ in range(n + 1)]
    for u, v in edges:
        adj[u][v] = adj[v][u] = True

    for i in range(1, n + 1):
        for k in range(1, n + 1):
            if i != k and not adj[i][k]:
                for j in range(1, n):
                    clauses.append([-var(i, j), -var(k, j + 1)])

    print(len(clauses), n * n)
    for c in clauses:
        print(" ".join(map(str, c)) + " 0")

if __name__ == "__main__":
    printEquisatisfiableSatFormula()
