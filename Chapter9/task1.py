n, m = [int(i) for i in input().split()]
a = []
for i in range(n):
    a.append([int(i) for i in input().split()])

ma = None
jma = None
ima = None

for j in range(n):
    for i in range(m):
        if ma == None:
            ma = a[j][i]
            jma = j
            ima = i
        elif ma < a[j][i]:
            ma = a[j][i]
            jma = j
            ima = i

print(jma, ima)
