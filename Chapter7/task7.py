a = list(map(int, input().split()))
x = int(input())
fl = False

for i in range(len(a)):
    if a[i] < x:
        fl = True
        break

if fl:
    print(i + 1)
else:
    print(len(a) + 1)
