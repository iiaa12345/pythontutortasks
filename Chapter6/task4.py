x = int(input())
y = int(input())
days = 1

while x < y:
    x += 0.1 * x
    days += 1

print(days)
