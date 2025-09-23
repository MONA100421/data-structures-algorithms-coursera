def optimal_summands(n):
    summands = []
    k = 1
    while n > 0:
        if n - k > k:
            summands.append(k)
            n -= k
            k += 1
        else:
            summands.append(n)
            break
    return summands


if __name__ == "__main__":
    n = int(input())
    s = optimal_summands(n)
    print(len(s))
    print(*s)
