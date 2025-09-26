#!/usr/bin/env python3
import sys
from collections import defaultdict

K = 12  # k-mer 長度（用來快速比對）

def read_input():
    reads = [line.strip() for line in sys.stdin if line.strip()]
    return reads

def overlap(a, b, min_length=30):
    """計算 a 的 suffix 與 b 的 prefix 最大重疊長度"""
    start = 0
    while True:
        start = a.find(b[:min_length], start)
        if start == -1:
            return 0
        if b.startswith(a[start:]):
            return len(a) - start
        start += 1

def build_kmer_index(reads, k):
    index = defaultdict(set)
    for i, read in enumerate(reads):
        prefix = read[:k]
        index[prefix].add(i)
    return index

def greedy_assembly(reads):
    n = len(reads)
    used = [False] * n
    genome = reads[0]
    used[0] = True
    last = 0

    index = build_kmer_index(reads, K)

    for _ in range(n - 1):
        best_olen, best_read = 0, None
        suffix = genome[-K:]
        for cand in index.get(suffix, []):
            if not used[cand]:
                olen = overlap(genome, reads[cand], min_length=K)
                if olen > best_olen:
                    best_olen, best_read = olen, cand
        if best_read is None:
            for j in range(n):
                if not used[j]:
                    best_read = j
                    best_olen = 0
                    break
        genome += reads[best_read][best_olen:]
        used[best_read] = True
        last = best_read
    return genome

def main():
    reads = read_input()
    genome = greedy_assembly(reads)
    print(genome)

if __name__ == "__main__":
    main()
