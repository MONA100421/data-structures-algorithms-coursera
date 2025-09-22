def get_change(n: int) -> int:
    coins = 0
    for d in (10, 5, 1):
        coins += n // d
        n %= d
    return coins


if __name__ == "__main__":
    n = int(input())
    print(get_change(n))
