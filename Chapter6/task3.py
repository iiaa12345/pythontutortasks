n = int(input())
a = 2
cnt = 1

if n == 1:
    print(0, 1)
else:
    while a * 2 <= n:
        a *= 2
        cnt += 1
    print(cnt, a)
