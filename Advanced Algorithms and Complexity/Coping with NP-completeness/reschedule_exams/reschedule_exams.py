# python3
import sys
sys.setrecursionlimit(10**7)

def read_input():
    n,m=map(int,sys.stdin.readline().split())
    colors=list(sys.stdin.readline().strip())
    edges=[[] for _ in range(n)]
    for _ in range(m):
        u,v=map(int,sys.stdin.readline().split())
        edges[u-1].append(v-1)
        edges[v-1].append(u-1)
    return n,m,colors,edges

def is_valid(u,c,new_colors,edges):
    for v in edges[u]:
        if new_colors[v]==c:
            return False
    return True

def dfs(u,colors,edges,new_colors):
    if u==len(colors): return True
    if colors[u] in "RGB":
        new_colors[u]=colors[u]
        if is_valid(u,new_colors[u],new_colors,edges):
            if dfs(u+1,colors,edges,new_colors): return True
        return False
    for c in "RGB":
        if is_valid(u,c,new_colors,edges):
            new_colors[u]=c
            if dfs(u+1,colors,edges,new_colors): return True
            new_colors[u]=""
    return False

def main():
    n,m,colors,edges=read_input()
    new_colors=[""]*n
    ok=dfs(0,colors,edges,new_colors)
    if not ok:
        print("Impossible")
    else:
        print("".join(new_colors))

if __name__=="__main__":
    main()
