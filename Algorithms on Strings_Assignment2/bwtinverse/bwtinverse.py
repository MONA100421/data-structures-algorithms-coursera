# python3
import sys
from collections import defaultdict

def inverse_bwt(bwt: str) -> str:
    """
    LF-mapping 逆 BWT。
    建立 first column (排序後) 與每個位置的 rank，據此做 LF 走訪。
    """
    n = len(bwt)
    first = sorted(bwt)

    occ_rank = defaultdict(int)
    ranks = [0]*n
    for i, ch in enumerate(bwt):
        occ_rank[ch] += 1
        ranks[i] = occ_rank[ch]

    starts = {}
    for i, ch in enumerate(first):
        if ch not in starts:
            starts[ch] = i

    row = bwt.index('$')
    result = []
    for _ in range(n):
        ch = bwt[row]
        result.append(ch)
        row = starts[ch] + ranks[row] - 1

    res = ''.join(reversed(result))
    return res

if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(inverse_bwt(bwt))
