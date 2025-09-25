import sys
import random
import statistics

class CountSketch:
    def __init__(self, d, w, seed=42):
        random.seed(seed)
        self.d = d
        self.w = w
        self.table = [[0] * w for _ in range(d)]
        # 生成 hash 和 sign 的隨機參數
        self.hash_a = [random.randint(1, 10**9) for _ in range(d)]
        self.hash_b = [random.randint(0, 10**9) for _ in range(d)]
        self.sign_a = [random.randint(1, 10**9) for _ in range(d)]
        self.sign_b = [random.randint(0, 10**9) for _ in range(d)]
        self.p = 10**9 + 7  # 大質數避免碰撞

    def _hash(self, row, x):
        return ((self.hash_a[row] * x + self.hash_b[row]) % self.p) % self.w

    def _sign(self, row, x):
        return 1 if ((self.sign_a[row] * x + self.sign_b[row]) % self.p) % 2 == 0 else -1

    def update(self, x, c=1):
        for row in range(self.d):
            j = self._hash(row, x)
            s = self._sign(row, x)
            self.table[row][j] += s * c

    def estimate(self, x):
        ests = []
        for row in range(self.d):
            j = self._hash(row, x)
            s = self._sign(row, x)
            ests.append(self.table[row][j] * s)
        return statistics.median(ests)

def main():
    data = sys.stdin.read().strip().split()
    n = int(data[0])      # number of insertions
    t = int(data[1])      # threshold
    idx = 2
    cs = CountSketch(d=5, w=200)   # 可依課程要求調 d, w

    # 第一組 (插入數據)
    for _ in range(n):
        id_, value = int(data[idx]), int(data[idx+1])
        idx += 2
        cs.update(id_, value)

    # 第二組 (刪除數據)
    for _ in range(n):
        id_, value = int(data[idx]), int(data[idx+1])
        idx += 2
        cs.update(id_, -value)

    # queries
    num_q = int(data[idx]); idx += 1
    queries = list(map(int, data[idx:idx+num_q]))

    for q in queries:
        if cs.estimate(q) >= t:
            print("1", end=" ")
        else:
            print("0", end=" ")

if __name__ == "__main__":
    main()
