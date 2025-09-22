def optimal_points(segments):
    segments.sort(key=lambda x: x[1])
    points = []
    current_point = None

    for l, r in segments:
        if current_point is None or not (l <= current_point <= r):
            current_point = r
            points.append(current_point)
    return points


if __name__ == "__main__":
    n = int(input())
    segments = [tuple(map(int, input().split())) for _ in range(n)]
    points = optimal_points(segments)
    print(len(points))
    print(*points)
