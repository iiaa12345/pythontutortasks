n, k = [int(i) for i in input().split()]
b = []

for i in range(k):
    b.append([int(i) for i in input().split()])

a = ["I" for i in range(n)]

for i in range(k):
    for j in range(b[i][0], b[i][1] + 1):
        a[j - 1] = "."

print("".join(a))
