h = int(input())
a = int(input())
b = int(input())
x = 0
d = 0

while x < h:
    d += 1
    x += a
    if x >= h:
        break
    x -= b

print(d)
