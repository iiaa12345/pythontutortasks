a = []
for i in range(8):
    a.append([int(i) for i in input().split()])

fl = False
for i in range(8):
    for j in range(i + 1, 8):
        if abs(a[i][0] - a[j][0]) == abs(a[i][1] - a[j][1]):
            fl = True
        elif a[i][0] == a[j][0] or a[i][1] == a[j][1]:
            fl = True

if fl:
    print("YES")
else:
    print("NO")
