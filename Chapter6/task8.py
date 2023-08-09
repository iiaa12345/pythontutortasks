a = 1
max_a = None
max_i = None
i = 0

while a != 0:
    a = int(input())
    if max_a == None:
        max_a = a
        max_i = i
    elif max_a < a:
        max_a = a
        max_i = i
    i += 1

print(max_i)
