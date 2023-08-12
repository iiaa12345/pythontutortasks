def power(a, n):
    c = 1
    if n > 0:
        for i in range(n):
            c *= a
    elif n < 0:
        for i in range(abs(n)):
            c /= a
    return c


a = float(input())
n = int(input())

print(power(a, n))
