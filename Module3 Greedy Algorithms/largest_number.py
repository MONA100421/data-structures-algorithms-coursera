from functools import cmp_to_key

def cmp(a: str, b: str) -> int:
    if a + b > b + a:
        return -1
    if a + b < b + a:
        return 1
    return 0

def largest_number(numbers):
    numbers = sorted(numbers, key=cmp_to_key(cmp))
    res = "".join(numbers)
    res = res.lstrip("0")
    return res or "0"


if __name__ == "__main__":
    _ = int(input())
    nums = input().split()
    print(largest_number(nums))
