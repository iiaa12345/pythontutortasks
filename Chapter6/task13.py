n = int(input())
i = 1
f = 1
pf = 0

while f < n:
    f, pf = f + pf, f
    i += 1

if f == n:
    print(i)
else:
    print(-1)
