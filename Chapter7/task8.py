a = list(map(int, input().split()))
p = a[0]
cnt = 1

for i in range(1, len(a)):
    if a[i] != p:
        p = a[i]
        cnt += 1

print(cnt)
