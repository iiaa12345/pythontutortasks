n = int(input())
su = 0

for i in range(n):
    su += int(input())

print((n * (n + 1) / 2) - su)
