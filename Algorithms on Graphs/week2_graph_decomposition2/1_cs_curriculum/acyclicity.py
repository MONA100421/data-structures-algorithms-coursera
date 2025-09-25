# Uses python3
import sys
sys.setrecursionlimit(10**7)

def has_cycle(adj):
    n = len(adj)
    # 0 = unvisited, 1 = in recursion stack (visiting), 2 = done
    color = [0] * n

    def dfs(u):
        color[u] = 1
        for v in adj[u]:
            if color[v] == 0:
                if dfs(v):
                    return True
            elif color[v] == 1:
                # back edge -> cycle
                return True
        color[u] = 2
        return False

    for u in range(n):
        if color[u] == 0 and dfs(u):
            return 1
    return 0


if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    n, m = data[0], data[1]
    edges = list(zip(data[2:2+2*m:2], data[3:2+2*m:2]))
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a-1].append(b-1)
    print(has_cycle(adj))
