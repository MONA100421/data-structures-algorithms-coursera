# python3
import sys
INF = 10**9

def read_data():
    n, m = map(int, sys.stdin.readline().split())
    graph = [[INF]*n for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        u -= 1; v -= 1
        graph[u][v] = min(graph[u][v], w)
    return graph

def floyd_warshall(graph):
    n = len(graph)
    dist = [row[:] for row in graph]
    for i in range(n):
        dist[i][i] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

def main():
    graph = read_data()
    dist = floyd_warshall(graph)
    for row in dist:
        print(" ".join(str(x if x < INF//2 else -1) for x in row))

if __name__ == "__main__":
    main()
