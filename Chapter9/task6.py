def swap_columns(a, i, j):
    for k in range(n):
        a[k][i], a[k][j] = a[k][j], a[k][i]
    
    return a


n, m = [int(i) for i in input().split()]
a = [[i for i in input().split()] for i in range(n)]
i, j = [int(i) for i in input().split()]

swap_columns(a, i, j)

for t in range(n):
    print(" ".join(a[t]))
