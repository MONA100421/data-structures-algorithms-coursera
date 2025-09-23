def compute_min_refills(distance, tank, stops):
    stops = [0] + stops + [distance]
    num_refills = 0
    current = 0
    n = len(stops) - 2

    while current <= n:
        last = current
        while current <= n and stops[current + 1] - stops[last] <= tank:
            current += 1
        if current == last:
            return -1
        if current <= n:
            num_refills += 1
    return num_refills


if __name__ == "__main__":
    d, m, n = map(int, input().split())
    stops = list(map(int, input().split())) if n > 0 else []
    print(compute_min_refills(d, m, stops))
