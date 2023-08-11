a = list(map(int, input().split()))

for i in range(1, len(a) // 2 * 2, 2):
    a[i], a[i - 1] = a[i - 1], a[i]

for i in range(len(a)):
    print(a[i])
