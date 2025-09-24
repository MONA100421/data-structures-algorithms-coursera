# python3

import sys


class Database:
    def __init__(self, row_counts):
        self.row_counts = row_counts[:]
        self.max_row_count = max(row_counts)
        n_tables = len(row_counts)
        self.ranks = [0] * n_tables
        self.parents = list(range(n_tables))

    def get_parent(self, table):
        if table != self.parents[table]:
            self.parents[table] = self.get_parent(self.parents[table])
        return self.parents[table]

    def merge(self, dst, src):
        dst_root = self.get_parent(dst)
        src_root = self.get_parent(src)
        if dst_root == src_root:
            return False

        if self.ranks[dst_root] < self.ranks[src_root]:
            dst_root, src_root = src_root, dst_root

        self.parents[src_root] = dst_root
        self.row_counts[dst_root] += self.row_counts[src_root]
        self.row_counts[src_root] = 0

        if self.ranks[dst_root] == self.ranks[src_root]:
            self.ranks[dst_root] += 1

        if self.row_counts[dst_root] > self.max_row_count:
            self.max_row_count = self.row_counts[dst_root]
        return True


def main():
    data = list(map(int, sys.stdin.read().split()))
    it = iter(data)
    n_tables, n_queries = next(it), next(it)
    counts = [next(it) for _ in range(n_tables)]
    db = Database(counts)
    out = []
    for _ in range(n_queries):
        dst, src = next(it) - 1, next(it) - 1
        db.merge(dst, src)
        out.append(str(db.max_row_count))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
