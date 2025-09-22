def get_optimal_value(capacity, values, weights):
    value = 0.0
    items = sorted(((v / w, v, w) for v, w in zip(values, weights)), reverse=True)
    for ratio, v, w in items:
        if capacity == 0:
            break
        take = min(w, capacity)
        value += ratio * take
        capacity -= take
    return value


if __name__ == "__main__":
    n, capacity = map(int, input().split())
    values, weights = [], []
    for _ in range(n):
        v, w = map(int, input().split())
        values.append(v)
        weights.append(w)
    print("{:.10f}".format(get_optimal_value(capacity, values, weights)))
