import sys

a, b = map(int, sys.stdin.read().split())
while b:
    a, b = b, a % b
print(a)
