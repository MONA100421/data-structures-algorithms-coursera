# python3

import sys

def printEquisatisfiableSatFormula():
    n, m = map(int, sys.stdin.readline().split())
    clauses = []

    # 讀取每筆投資 (company, project)
    investments = []
    for _ in range(m):
        company, project = map(int, sys.stdin.readline().split())
        investments.append((company, project))

    # 每個公司最多一筆
    company_to_edges = {}
    for i, (c, p) in enumerate(investments):
        company_to_edges.setdefault(c, []).append(i + 1)

    for edges in company_to_edges.values():
        for i in range(len(edges)):
            for j in range(i + 1, len(edges)):
                clauses.append([-edges[i], -edges[j]])

    # 每個 project 至少一筆
    project_to_edges = {}
    for i, (c, p) in enumerate(investments):
        project_to_edges.setdefault(p, []).append(i + 1)

    for edges in project_to_edges.values():
        clauses.append(edges)

    # 輸出 CNF
    print(len(clauses), m)
    for clause in clauses:
        print(" ".join(map(str, clause)) + " 0")

if __name__ == "__main__":
    printEquisatisfiableSatFormula()
