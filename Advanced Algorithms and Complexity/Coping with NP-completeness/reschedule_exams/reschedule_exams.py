# python3
import sys
from collections import deque

def reschedule_exams(n, edges):
    graph = [[] for _ in range(n)]
    for a, b in edges:
        a -= 1; b -= 1
        graph[a].append(b)
        graph[b].append(a)

    color = [-1]*n
    for start in range(n):
        if color[start] == -1:
            color[start] = 0
            q = deque([start])
            while q:
                v = q.popleft()
                for u in graph[v]:
                    if color[u] == -1:
                        color[u] = 1 - color[v]
                        q.append(u)
                    elif color[u] == color[v]:
                        return None
    return color

def main():
    n, m = map(int, sys.stdin.readline().split())
    edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]
    result = reschedule_exams(n, edges)
    if result is None:
        print("IMPOSSIBLE")
    else:
        print(" ".join(str(x+1) for x in result))

if __name__ == "__main__":
    main()
