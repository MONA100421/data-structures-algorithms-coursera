# python3
import sys
sys.setrecursionlimit(10**7)

def dfs(v, parent, graph, used, order):
    used[v] = True
    for u in graph[v]:
        if not used[u]:
            dfs(u, v, graph, used, order)
    order.append(v)

def plan_party(n, edges):
    graph = [[] for _ in range(n)]
    rgraph = [[] for _ in range(n)]
    for a, b in edges:
        a -= 1; b -= 1
        graph[a].append(b)
        rgraph[b].append(a)

    used = [False]*n
    order = []
    for v in range(n):
        if not used[v]:
            dfs(v, -1, graph, used, order)

    comp = [-1]*n
    label = 0
    def rdfs(v, label):
        comp[v] = label
        for u in rgraph[v]:
            if comp[u] == -1:
                rdfs(u, label)

    for v in reversed(order):
        if comp[v] == -1:
            rdfs(v, label)
            label += 1

    return label

def main():
    n, m = map(int, sys.stdin.readline().split())
    edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]
    print(plan_party(n, edges))

if __name__ == "__main__":
    main()
