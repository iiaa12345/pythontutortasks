n = int(input())
s = 0

for i in range(n - 1):
    s += int(input())

print((n * (n + 1) / 2) - s)
