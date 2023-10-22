n, m = [int(i) for i in input().split()]
a = set()
b = set()
for i in range(n):
    a.add(input())
for i in range(m):
    b.add(input())

print(len(a & b))
print(" ".join(sorted(a & b, key=int)))
print(len(a - b))
print(" ".join(sorted(a - b, key=int)))
print(len(b - a))
print(" ".join(sorted(b - a, key=int)))
