def distance(x1, x2, y1, y2):
    return (abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) ** 0.5


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

print(distance(x1, x2, y1, y2))
