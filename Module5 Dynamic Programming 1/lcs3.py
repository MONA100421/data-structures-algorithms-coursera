def lcs3(first_sequence, second_sequence, third_sequence):
    a, b, c = first_sequence, second_sequence, third_sequence
    n, m, q = len(a), len(b), len(c)
    dp = [[[0]*(q+1) for _ in range(m+1)] for __ in range(n+1)]
    for i in range(1, n+1):
        ai = a[i-1]
        for j in range(1, m+1):
            bj = b[j-1]
            for k in range(1, q+1):
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1 if ai == bj and ai == c[k-1] \
                              else max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
    return dp[n][m][q]

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))
