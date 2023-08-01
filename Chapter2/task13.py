n = int(input())
m = int(input())
x = int(input())
y = int(input())

if n > m:
    dx = m - x
    dy = n - y
else:
    dx = n - x
    dy = m - y

min_x = dx
if x < dx:
    min_x = x

min_y = dy
if y < dy:
    min_y = y

if min_x < min_y:
    print(min_x)
else:
    print(min_y)
