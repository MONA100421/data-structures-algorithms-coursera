# use python3
import sys
from collections import defaultdict, deque

def read_input():
    kmers = [line.strip() for line in sys.stdin if line.strip()]
    return kmers

def build_debruijn(kmers):
    edges = defaultdict(deque)
    for kmer in kmers:
        prefix = kmer[:-1]
        suffix = kmer[1:]
        edges[prefix].append(suffix)
    return edges

def eulerian_cycle(edges):
    start = next(iter(edges))
    stack = [start]
    path = []
    while stack:
        v = stack[-1]
        if edges[v]:
            stack.append(edges[v].popleft())
        else:
            path.append(stack.pop())
    return path[::-1]

def main():
    kmers = read_input()
    k = len(kmers[0])
    edges = build_debruijn(kmers)
    cycle = eulerian_cycle(edges)
    genome = cycle[0]
    for node in cycle[1:]:
        genome += node[-1]
    print(genome[:-k+1])  # make circular

if __name__ == "__main__":
    main()
