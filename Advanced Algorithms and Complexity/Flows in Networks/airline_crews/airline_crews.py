# python3
class MaxMatching:
    def read_data(self):
        n, m = map(int, input().split())
        adj_matrix = [list(map(int, input().split())) for _ in range(n)]
        return adj_matrix

    def write_response(self, matching):
        line = [str(-1 if x == -1 else x + 1) for x in matching]
        print(' '.join(line))

    def try_kuhn(self, v, adj_matrix, used, mt):
        if used[v]:
            return False
        used[v] = True
        for j in range(len(adj_matrix[v])):
            if adj_matrix[v][j]:
                if mt[j] == -1 or self.try_kuhn(mt[j], adj_matrix, used, mt):
                    mt[j] = v
                    return True
        return False

    def find_matching(self, adj_matrix):
        n = len(adj_matrix)
        m = len(adj_matrix[0])
        mt = [-1] * m
        for v in range(n):
            used = [False] * n
            self.try_kuhn(v, adj_matrix, used, mt)
        ans = [-1] * n
        for j in range(m):
            if mt[j] != -1:
                ans[mt[j]] = j
        return ans

    def solve(self):
        adj_matrix = self.read_data()
        matching = self.find_matching(adj_matrix)
        self.write_response(matching)


if __name__ == '__main__':
    max_matching = MaxMatching()
    max_matching.solve()
