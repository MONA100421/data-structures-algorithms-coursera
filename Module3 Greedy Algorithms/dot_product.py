def max_dot_product(a, b):
    a.sort()
    b.sort()
    return sum(x * y for x, y in zip(a, b))


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(max_dot_product(a, b))
