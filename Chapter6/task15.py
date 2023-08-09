a = 1
s = 0
cnt = 0
s2 = 0

while a != 0:
    a = int(input())
    if a != 0:
        s += a
        s2 += a ** 2
        cnt += 1

print(((s2 - s ** 2 / cnt) / (cnt - 1)) ** 0.5)
