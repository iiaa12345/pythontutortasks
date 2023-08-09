a = int(input())
cnt = 0

while a != 0:
    pa = a
    a = int(input())
    if a != 0 and a > pa:
        cnt += 1

print(cnt)
