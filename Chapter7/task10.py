a = [int(i) for i in input().split()]
max_a = a[0]
min_a = a[0]
imax_a = 0
imin_a = 0

for i in range(len(a)):
    if a[i] > max_a:
        max_a = a[i]
        imax_a = i
    if a[i] < min_a:
        min_a = a[i]
        imin_a = i

a[imax_a], a[imin_a] = a[imin_a], a[imax_a]

print(' '.join([str(i) for i in a]))
