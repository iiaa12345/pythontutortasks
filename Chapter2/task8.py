a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a == c:
    if abs(b - d) == 1:
        print("YES")
    else:
        print("NO")
elif b == d:
    if abs(a - c) == 1:
        print("YES")
    else:
        print("NO")
elif abs(a - c) == 1:
    if abs(b - d) == 1:
        print("YES")
    else:
        print("NO")
elif abs(b - d) == 1:
    if abs(a - c == 1):
        print("YES")
    else:
        print("NO")
else:
    print("NO")
