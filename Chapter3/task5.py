n = int(input())

t = 9 * 60
t += 45 * n

if n % 2 == 0:
    t += (n // 2) * 5
    t += (n // 2 - 1) * 15
else:
    t += (n // 2) * 5
    t += (n // 2) * 15

print(t // 60, t % 60)
