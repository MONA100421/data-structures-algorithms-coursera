import sys
import random
import hashlib

class CountSketch:
    def __init__(self, num_rows, num_buckets):
        self.num_rows = num_rows
        self.num_buckets = num_buckets
        self.tables = [[0] * num_buckets for _ in range(num_rows)]
        # 每一列有兩個 hash：一個決定桶子位置，一個決定正負號
        self.hash_funcs = [self._make_hash(i) for i in range(num_rows)]
        self.sign_funcs = [self._make_sign_hash(i + 1000) for i in range(num_rows)]

    def _make_hash(self, seed):
        def h(x):
            return int(hashlib.md5((str(x) + str(seed)).encode()).hexdigest(), 16) % self.num_buckets
        return h

    def _make_sign_hash(self, seed):
        def s(x):
            return 1 if int(hashlib.md5((str(x) + str(seed)).encode()).hexdigest(), 16) % 2 == 0 else -1
        return s

    def update(self, key, value):
        for r in range(self.num_rows):
            idx = self.hash_funcs[r](key)
            sign = self.sign_funcs[r](key)
            self.tables[r][idx] += sign * value

    def estimate(self, key):
        estimates = []
        for r in range(self.num_rows):
            idx = self.hash_funcs[r](key)
            sign = self.sign_funcs[r](key)
            estimates.append(sign * self.tables[r][idx])
        # 取中位數避免 outlier
        estimates.sort()
        return estimates[len(estimates)//2]


def main():
    data = sys.stdin.read().strip().split()
    n = int(data[0])   # number of updates
    t = int(data[1])   # threshold

    cs = CountSketch(num_rows=5, num_buckets=2003)

    idx = 2
    for _ in range(n):
        key, val = int(data[idx]), int(data[idx+1])
        cs.update(key, val)
        idx += 2

    for _ in range(n):
        key, val = int(data[idx]), int(data[idx+1])
        cs.update(key, -val)
        idx += 2

    q = int(data[idx]); idx += 1
    queries = list(map(int, data[idx:idx+q]))

    for key in queries:
        if cs.estimate(key) >= t:
            print("1 ", end="")
        else:
            print("0 ", end="")

if __name__ == "__main__":
    main()
