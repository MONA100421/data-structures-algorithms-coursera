import sys

a, b = map(int, sys.stdin.read().split())

x, y = a, b
while y:
    x, y = y, x % y
g = x

print(a // g * b)
