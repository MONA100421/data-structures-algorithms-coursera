# python3
class StockCharts:
    def read_data(self):
        n, k = map(int, input().split())
        stock_data = [list(map(int, input().split())) for _ in range(n)]
        return stock_data

    def write_response(self, result):
        print(result)

    def can_be_above(self, s1, s2):
        return all(x < y for x, y in zip(s1, s2))

    def min_charts(self, stock_data):
        n = len(stock_data)
        adj = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j and self.can_be_above(stock_data[i], stock_data[j]):
                    adj[i].append(j)

        mt = [-1] * n

        def try_kuhn(v, used):
            if used[v]:
                return False
            used[v] = True
            for to in adj[v]:
                if mt[to] == -1 or try_kuhn(mt[to], used):
                    mt[to] = v
                    return True
            return False

        for v in range(n):
            used = [False] * n
            try_kuhn(v, used)

        matching_size = sum(1 for x in mt if x != -1)
        return n - matching_size

    def solve(self):
        stock_data = self.read_data()
        result = self.min_charts(stock_data)
        self.write_response(result)


if __name__ == '__main__':
    stock_charts = StockCharts()
    stock_charts.solve()
