n = int(input())

k = n // 60
while k > 23:
    k -= 24

print(k)
print(n % 60)