a = 1
max_a = None
cnt = 0

while a != 0:
    a = int(input())
    if max_a == None:
        max_a = a
        cnt = 1
    elif max_a < a:
        max_a = a
        cnt = 1
    elif max_a == a:
        cnt += 1

print(cnt)
