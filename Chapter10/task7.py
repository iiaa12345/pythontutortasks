n = int(input())
x = set(i for i in input().split())

a = set(str(i) for i in range(1, n + 1))
b = set()

while "HELP" not in x:
    f = input()
    if f == "YES":
        a &= x
    else:
        b |= x
    x = set(i for i in input().split())

a -= b
print(" ".join(a))
