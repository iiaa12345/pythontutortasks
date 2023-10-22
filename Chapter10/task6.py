n = int(input())
a = set()

for i in range(n):
    x = input().split()
    for j in range(len(x)):
        a.add(x[j])

print(len(a))
