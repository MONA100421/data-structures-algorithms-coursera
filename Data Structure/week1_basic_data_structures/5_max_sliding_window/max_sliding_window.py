# python3
from collections import deque


def max_sliding_window(sequence, m):
    dq = deque()    # store indices; sequence[dq] is decreasing
    ans = []

    for i, x in enumerate(sequence):
        while dq and sequence[dq[-1]] <= x:
            dq.pop()

        dq.append(i)

        if dq[0] <= i - m:
            dq.popleft()

        if i >= m - 1:
            ans.append(sequence[dq[0]])

    return ans


if __name__ == '__main__':
    n = int(input())
    seq = [int(i) for i in input().split()]
    assert len(seq) == n
    m = int(input())
    print(*max_sliding_window(seq, m))
