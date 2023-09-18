n, m = [int(i) for i in input().split()]
a = [["." for i in range(m)] for i in range(n)]

for j in range(n):
    if j % 2 == 0:
        for i in range(1, m, 2):
            a[j][i] = "*"
    else:
        for i in range(0, m, 2):
            a[j][i] = "*"

    print(" ".join(a[j]))
