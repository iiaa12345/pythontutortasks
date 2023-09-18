n = int(input())
a = [["2" for i in range(n)] for i in range(n)]

for j in range(n):
    for i in range(j + 1, n + 1):
        if j == i - 1:
            a[j][n - i] = "1"
        else:
            a[j][n - i] = "0"

    print(" ".join(a[j]))
