def change(money):
    coins = (1, 3, 4)
    dp = [0] + [10**9] * money
    for m in range(1, money + 1):
        for c in coins:
            if m >= c and dp[m - c] + 1 < dp[m]:
                dp[m] = dp[m - c] + 1
    return dp[money]


if __name__ == '__main__':
    m = int(input())
    print(change(m))
