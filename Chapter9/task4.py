n = int(input())
a = [[] for i in range(n)]

for j in range(n):
    for i in range(n):
        a[j].append(str(abs(j - i)))

    print(" ".join(a[j]))
