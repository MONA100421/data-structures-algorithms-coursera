#!/usr/bin/env python3
import sys
from collections import defaultdict

K = 12  # k-mer 長度（用來快速比對）
MISMATCH_TOL = 5  # 允許 mismatch 數量（5% of 100bp）

def read_input():
    reads = [line.strip() for line in sys.stdin if line.strip()]
    return reads

def approx_overlap(a, b, min_length=30):
    """計算 a 的 suffix 與 b 的 prefix 最大允許 mismatch 的重疊長度"""
    max_olen = 0
    for olen in range(min_length, len(a) + 1):
        mismatches = sum(1 for x, y in zip(a[-olen:], b[:olen]) if x != y)
        if mismatches <= MISMATCH_TOL:
            max_olen = olen
    return max_olen

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
                olen = approx_overlap(genome, reads[cand], min_length=K)
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
