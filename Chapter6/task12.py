n = int(input())
f = 1
pf = 0

for i in range(n):
    f, pf = f + pf, f

print(pf)
