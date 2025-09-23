def compute_operations(n):
    dp = [0] * (n + 1)
    prev = [0] * (n + 1)
    for x in range(2, n + 1):
        dp[x] = dp[x - 1] + 1; prev[x] = x - 1
        if x % 2 == 0 and dp[x // 2] + 1 < dp[x]:
            dp[x] = dp[x // 2] + 1; prev[x] = x // 2
        if x % 3 == 0 and dp[x // 3] + 1 < dp[x]:
            dp[x] = dp[x // 3] + 1; prev[x] = x // 3
    seq, cur = [], n
    while cur > 1:
        seq.append(cur); cur = prev[cur]
    seq.append(1); seq.reverse()
    return seq


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
