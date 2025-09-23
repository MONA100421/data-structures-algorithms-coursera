import sys
sys.setrecursionlimit(10**7)

def merge_count(a, tmp, left, mid, right):
    i, j, k = left, mid + 1, left
    inv = 0
    while i <= mid and j <= right:
        if a[i] <= a[j]:
            tmp[k] = a[i]; i += 1
        else:
            tmp[k] = a[j]; j += 1
            inv += (mid - i + 1)
        k += 1
    while i <= mid:
        tmp[k] = a[i]; i += 1; k += 1
    while j <= right:
        tmp[k] = a[j]; j += 1; k += 1
    a[left:right+1] = tmp[left:right+1]
    return inv

def sort_count(a, tmp, left, right):
    if left >= right: 
        return 0
    mid = (left + right) // 2
    inv = sort_count(a, tmp, left, mid)
    inv += sort_count(a, tmp, mid + 1, right)
    inv += merge_count(a, tmp, left, mid, right)
    return inv

if __name__ == '__main__':
    data = list(map(int, open(0).read().split()))
    n = data[0]
    arr = data[1:1+n]
    tmp = [0]*n
    print(sort_count(arr, tmp, 0, n-1))
