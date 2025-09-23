import random
import sys
sys.setrecursionlimit(10**7)

def partition3(a, l, r):
    # Dutch National Flag 3-way partition
    pivot = a[l]
    lt, i, gt = l, l + 1, r
    while i <= gt:
        if a[i] < pivot:
            a[lt], a[i] = a[i], a[lt]
            lt += 1
            i += 1
        elif a[i] > pivot:
            a[i], a[gt] = a[gt], a[i]
            gt -= 1
        else:
            i += 1
    return lt, gt

def randomized_quick_sort(a, l, r):
    while l < r:
        k = random.randint(l, r)
        a[l], a[k] = a[k], a[l]
        m1, m2 = partition3(a, l, r)
        # Tail recursion optimization: sort smaller side first
        if (m1 - l) < (r - m2):
            randomized_quick_sort(a, l, m1 - 1)
            l = m2 + 1
        else:
            randomized_quick_sort(a, m2 + 1, r)
            r = m1 - 1

if __name__ == '__main__':
    data = list(map(int, open(0).read().split()))
    n = data[0]
    arr = data[1:1+n]
    randomized_quick_sort(arr, 0, len(arr) - 1)
    print(*arr)
