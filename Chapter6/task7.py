a = 1
s = 0
cnt = 0

while a != 0:
    a = int(input())
    s += a
    if a != 0:
        cnt += 1

print(s / cnt)
