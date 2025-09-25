# python3
import sys
sys.setrecursionlimit(10**7)

def circuit_design(n, clauses):
    graph = [[] for _ in range(2*n)]
    for x, y in clauses:
        def var_index(v):
            if v > 0:
                return 2*(v-1)
            else:
                return 2*(-v-1)+1
        graph[var_index(-x)].append(var_index(y))
        graph[var_index(-y)].append(var_index(x))

    visited = [False]*(2*n)
    order = []

    def dfs(v):
        visited[v] = True
        for u in graph[v]:
            if not visited[u]:
                dfs(u)
        order.append(v)

    for v in range(2*n):
        if not visited[v]:
            dfs(v)

    rgraph = [[] for _ in range(2*n)]
    for v in range(2*n):
        for u in graph[v]:
            rgraph[u].append(v)

    comp = [-1]*(2*n)

    def rdfs(v, label):
        comp[v] = label
        for u in rgraph[v]:
            if comp[u] == -1:
                rdfs(u, label)

    label = 0
    for v in reversed(order):
        if comp[v] == -1:
            rdfs(v, label)
            label += 1

    assignment = [False]*n
    for i in range(n):
        if comp[2*i] == comp[2*i+1]:
            return None
        assignment[i] = comp[2*i] > comp[2*i+1]
    return assignment


def main():
    n, m = map(int, sys.stdin.readline().split())
    clauses = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]
    assignment = circuit_design(n, clauses)
    if assignment is None:
        print("UNSATISFIABLE")
    else:
        print("SATISFIABLE")
        print(" ".join([str(i+1 if val else -(i+1)) for i, val in enumerate(assignment)]))

if __name__ == "__main__":
    main()
