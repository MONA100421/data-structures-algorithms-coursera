from sys import stdin

def partition3(values):
    total = sum(values)
    if total % 3 != 0:
        return 0
    target = total // 3
    # dp[s1][s2] = whether it's possible to reach sums (s1, s2)
    dp = [[False]*(target+1) for _ in range(target+1)]
    dp[0][0] = True
    for a in values:
        new = [row[:] for row in dp]
        for s1 in range(target, -1, -1):
            for s2 in range(target, -1, -1):
                if dp[s1][s2]:
                    if s1 + a <= target:
                        new[s1 + a][s2] = True
                    if s2 + a <= target:
                        new[s1][s2 + a] = True
        dp = new
    return 1 if dp[target][target] else 0


if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))
