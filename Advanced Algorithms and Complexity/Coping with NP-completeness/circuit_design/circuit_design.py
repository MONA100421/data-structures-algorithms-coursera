# python3
import sys
sys.setrecursionlimit(10**7)

def read_input():
    n, m = map(int, sys.stdin.readline().split())
    clauses = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]
    return n, m, clauses

def var_index(x, n):
    return 2*(abs(x)-1) ^ (0 if x > 0 else 1)

def solve_2sat(n, m, clauses):
    N = 2*n
    graph = [[] for _ in range(N)]
    rgraph = [[] for _ in range(N)]

    def add_edge(u,v):
        graph[u].append(v)
        rgraph[v].append(u)

    for a,b in clauses:
        add_edge(var_index(-a,n), var_index(b,n))
        add_edge(var_index(-b,n), var_index(a,n))

    visited = [False]*N
    order = []
    for i in range(N):
        if not visited[i]:
            stack=[(i,0)]
            while stack:
                u,state=stack.pop()
                if state==0:
                    if visited[u]: continue
                    visited[u]=True
                    stack.append((u,1))
                    for v in graph[u]:
                        if not visited[v]:
                            stack.append((v,0))
                else:
                    order.append(u)

    comp=[-1]*N
    label=0
    for u in reversed(order):
        if comp[u]==-1:
            stack=[u]
            comp[u]=label
            while stack:
                v=stack.pop()
                for w in rgraph[v]:
                    if comp[w]==-1:
                        comp[w]=label
                        stack.append(w)
            label+=1

    assignment=[False]*n
    for i in range(n):
        if comp[2*i]==comp[2*i+1]:
            return False,[]
        assignment[i]=comp[2*i]>comp[2*i+1]

    result=[]
    for i in range(n):
        result.append(i+1 if assignment[i] else -(i+1))
    return True,result

def main():
    n,m,clauses=read_input()
    sat,assignment=solve_2sat(n,m,clauses)
    if not sat:
        print("UNSATISFIABLE")
    else:
        print("SATISFIABLE")
        print(" ".join(map(str,assignment)))

if __name__=="__main__":
    main()
