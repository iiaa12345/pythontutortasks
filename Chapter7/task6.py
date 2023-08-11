a = list(map(int, input().split()))
ma = a[0]
ima = 0

for i in range(len(a)):
    if a[i] > ma:
        ma = a[i]
        ima = i

print(ma, ima)
