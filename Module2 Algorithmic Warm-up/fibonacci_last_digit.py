import sys

n = int(sys.stdin.read())
n %= 60
a, b = 0, 1
for _ in range(n):
    a, b = b % 10, (a + b) % 10
print(a)

