a = 1
max_a = 0
pmax_a = 0

while a != 0:
    a = int(input())

    if max_a < a:
        pmax_a = max_a
        max_a = a
    elif a > pmax_a:
        pmax_a = a

print(pmax_a)
