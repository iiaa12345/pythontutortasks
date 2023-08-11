a = [int(i) for i in input().split()]
b = []

for i in range(len(a)):
    if a.count(a[i]) == 1:
        b.append(a[i])

print(" ".join([str(i) for i in b]))
