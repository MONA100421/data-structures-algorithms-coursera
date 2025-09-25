
# Bidirectional BFS for friend suggestion (unweighted undirected graph)
import sys
sys.setrecursionlimit(10**7)

def readints():
    return list(map(int, sys.stdin.readline().split()))

def bidir_bfs(adj, s, t):
    if s == t:
        return 0
    n = len(adj)
    from collections import deque
    q1 = deque([s]); q2 = deque([t])
    dist1 = [-1]*n; dist2 = [-1]*n
    dist1[s] = 0; dist2[t] = 0
    visited1 = set([s]); visited2 = set([t])
    while q1 and q2:
        # Expand smaller frontier
        if len(q1) <= len(q2):
            for _ in range(len(q1)):
                u = q1.popleft()
                for v in adj[u]:
                    if dist1[v] == -1:
                        dist1[v] = dist1[u] + 1
                        if dist2[v] != -1:
                            return dist1[v] + dist2[v]
                        q1.append(v)
        else:
            for _ in range(len(q2)):
                u = q2.popleft()
                for v in adj[u]:
                    if dist2[v] == -1:
                        dist2[v] = dist2[u] + 1
                        if dist1[v] != -1:
                            return dist1[v] + dist2[v]
                        q2.append(v)
    return -1

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(map(int, data))
    n = next(it); m = next(it)
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = next(it)-1; v = next(it)-1
        adj[u].append(v); adj[v].append(u)
    q = next(it)
    out_lines = []
    for _ in range(q):
        s = next(it)-1; t = next(it)-1
        out_lines.append(str(bidir_bfs(adj,s,t)))
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()
