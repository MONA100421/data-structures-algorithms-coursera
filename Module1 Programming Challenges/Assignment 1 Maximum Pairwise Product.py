import sys
from typing import List


def max_pairwise_product_fast(nums: List[int]) -> int:
    n = len(nums)
    if n < 2:
        raise ValueError("Need at least two numbers")

    max1_i = 0
    for i in range(1, n):
        if nums[i] > nums[max1_i]:
            max1_i = i

    max2_i = 0 if max1_i != 0 else 1
    for i in range(n):
        if i == max1_i:
            continue
        if nums[i] > nums[max2_i]:
            max2_i = i

    return nums[max1_i] * nums[max2_i]


def max_pairwise_product_naive(nums: List[int]) -> int:
    best = 0
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            best = max(best, nums[i] * nums[j])
    return best


def parse_input_from_stdin() -> List[int]:
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        raise ValueError("No input provided")

    n = data[0]
    nums = data[1:1 + n]
    if len(nums) != n:
        raise ValueError(f"Expected {n} numbers, got {len(nums)}.")
    return nums


def main():
    nums = parse_input_from_stdin()
    print(max_pairwise_product_fast(nums))


if __name__ == "__main__":
    main()
