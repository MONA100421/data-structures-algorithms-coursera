# python3

def printEquisatisfiableSatFormula():
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]

    def var(i, c):
        return (i - 1) * 3 + c

    clauses = []

    # 每個頂點至少一個顏色
    for i in range(1, n + 1):
        clauses.append([var(i, 1), var(i, 2), var(i, 3)])

    # 每個頂點最多一個顏色
    for i in range(1, n + 1):
        for c1 in range(1, 4):
            for c2 in range(c1 + 1, 4):
                clauses.append([-var(i, c1), -var(i, c2)])

    # 相鄰頂點不能同色
    for u, v in edges:
        for c in range(1, 4):
            clauses.append([-var(u, c), -var(v, c)])

    print(len(clauses), n * 3)
    for c in clauses:
        print(" ".join(map(str, c)) + " 0")

if __name__ == "__main__":
    printEquisatisfiableSatFormula()
