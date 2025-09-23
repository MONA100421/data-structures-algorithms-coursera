from sys import stdin

def maximum_gold(capacity, weights):
    # 0/1 knapsack where value == weight; return maximum achievable weight <= capacity
    dp = [0] * (capacity + 1)
    for w in weights:
        for c in range(capacity, w - 1, -1):
            if dp[c - w] + w > dp[c]:
                dp[c] = dp[c - w] + w
    return dp[capacity]


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n
    print(maximum_gold(input_capacity, input_weights))
