a = 1
pa = 0
cnt = 0
mcnt = 0

while a != 0:
    a = int(input())
    if pa != a:
        if mcnt < cnt:
            mcnt = cnt
        cnt = 1
    elif pa == a:
        cnt += 1
    pa = a

print(mcnt)
