a = list(map(int, input().split()))
cnt = 0

for i in range(1, len(a) - 1):
    if a[i + 1] < a[i] and a[i] > a[i - 1]:
        cnt += 1

print(cnt)
