# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    a = data[1:1 + n]
    m = data[1 + n]
    b = data[2 + n:]
    assert len(b) == m
    res = [str(binary_search(a, x)) for x in b]
    print(' '.join(res))

if __name__ == '__main__':
    main()
