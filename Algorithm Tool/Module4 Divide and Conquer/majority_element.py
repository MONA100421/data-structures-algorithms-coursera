def has_majority(a):
    # Boyer-Moore majority vote + verification
    count = 0
    cand = None
    for x in a:
        if count == 0:
            cand = x
            count = 1
        elif x == cand:
            count += 1
        else:
            count -= 1
    if cand is None:
        return 0
    return 1 if a.count(cand) > len(a) // 2 else 0


if __name__ == '__main__':
    n, *rest = list(map(int, open(0).read().split()))
    arr = rest[:n]
    print(has_majority(arr))
