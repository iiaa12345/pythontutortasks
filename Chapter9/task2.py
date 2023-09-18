n = int(input())
a = [["." for i in range(n)] for i in range(n)]

for j in range(n):
    for i in range(n):
        if i == 0 + j:
            a[j][i] = "*"
        elif i == n - j - 1:
            a[j][i] = "*"
        elif i == n // 2:
            a[j][i] = "*"
        elif j == n // 2:
            a[j][i] = "*"
    
    print(" ".join(a[j]))
