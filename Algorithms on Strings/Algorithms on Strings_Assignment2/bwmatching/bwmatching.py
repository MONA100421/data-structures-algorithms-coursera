# python3
import sys
from collections import defaultdict

def PreprocessBWT(bwt):
    """
    回傳:
      starts: 每個字元在排序後 first column 的第一個出現位置
      occ_counts_before: 對每個字元 C，給出長度 n 的陣列，其中
         occ_counts_before[C][i] = bwt[0..i]（含 i）中 C 的出現次數
         （注意：是「包含 i」的前綴計數）
    """
    n = len(bwt)
    alphabet = sorted(set(bwt))
    # starts
    first = sorted(bwt)
    starts = {}
    for i, ch in enumerate(first):
        if ch not in starts:
            starts[ch] = i

    # occ_counts_before（inclusive prefix counts）
    occ_counts_before = {c: [0]*n for c in alphabet}
    running = defaultdict(int)
    for i, ch in enumerate(bwt):
        running[ch] += 1
        for c in alphabet:
            occ_counts_before[c][i] = running[c]
    return starts, occ_counts_before

def _occ_inclusive(occ_counts_before, ch, pos):
    if pos < 0:
        return 0
    return occ_counts_before.get(ch, [0])[pos]

def CountOccurrences(pattern, bwt, starts, occ_counts_before):
    """
    從 BWT 進行 backward search，回傳 pattern 在原字串中的出現次數。
    使用「包含 pos」的 occ_counts_before 版本：
      top = starts[c] + occ[c][top-1]
      bottom = starts[c] + occ[c][bottom] - 1
    """
    top, bottom = 0, len(bwt) - 1
    i = len(pattern) - 1
    while top <= bottom and i >= 0:
        symbol = pattern[i]
        i -= 1
        if symbol not in starts:
            return 0
        top = starts[symbol] + _occ_inclusive(occ_counts_before, symbol, top - 1)
        bottom = starts[symbol] + _occ_inclusive(occ_counts_before, symbol, bottom) - 1
    if i < 0 and top <= bottom:
        return bottom - top + 1
    return 0

if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    pattern_count = int(sys.stdin.readline().strip())
    patterns = sys.stdin.readline().strip().split()
    starts, occ_counts_before = PreprocessBWT(bwt)
    occurrence_counts = [CountOccurrences(p, bwt, starts, occ_counts_before)
                         for p in patterns]
    print(' '.join(map(str, occurrence_counts)))
